import os
import pandas as pd
import numpy as np
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml
import re
from tqdm import tqdm
import multiprocessing as mp
import time
import random
import datetime
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from skimage import io
from sklearn.decomposition import PCA
from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn


def recommend_tracks(df, playvec, sp):
    # Select numeric features
    numeric_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                        'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'Track_release_date', 'Track_pop', 'Artist_pop']

    # Extract numeric features for PCA
    df_new_numeric = df[numeric_features]
    playvec_new_numeric = playvec[numeric_features]

    # Initialize and fit PCA
    pca = PCA(n_components=0.95)
    pca.fit(df_new_numeric)

    # Transform both df and playvec numeric features using PCA
    df_pca = pca.transform(df_new_numeric)
    playvec_pca = pca.transform(playvec_new_numeric)

    # Convert PCA components to DataFrame
    df_pca_df = pd.DataFrame(df_pca, index=df.index)
    playvec_pca_df = pd.DataFrame(playvec_pca, index=playvec.index)

    # Calculate cosine similarity for PCA and genres
    df['sim_pca'] = cosine_similarity(df_pca_df, playvec_pca_df)
    df['sim_genres'] = cosine_similarity(df.loc[:, df.columns.str.startswith(
        'genre')], playvec.loc[:, playvec.columns.str.startswith('genre')])
    df['sim_combined'] = (df['sim_pca'] + df['sim_genres']) / 2

    # Sort based on similarity score
    df = df.sort_values(['sim_genres', 'sim_combined'],
                        ascending=False, kind='stable')

    # Get the list of top track URIs
    top_tracks = df.groupby('artist_uri').head(2).track_uri.head(20)

    # Fetch track details from Spotify
    track_details = sp.tracks(top_tracks[0:20])
    Fresult = pd.DataFrame()
    for i in range(20):
        result = pd.DataFrame([i], columns=['Index'])
        result['track_name'] = track_details['tracks'][i]['name']
        result['artist_name'] = track_details['tracks'][i]['artists'][0]['name']
        result['pop'] = track_details['tracks'][i]["popularity"]
        Fresult = pd.concat([Fresult, result], axis=0)

    return Fresult.reset_index(drop=True)
