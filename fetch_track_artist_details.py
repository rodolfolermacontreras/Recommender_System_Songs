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
import logging


def fetch_track_artist_details(spotify_client, track_ids_uni, artist_id_uni):
    logging.debug("Entered fetch_track_artist_details")
    audio_features = pd.DataFrame()
    track_details = pd.DataFrame()
    artist_details = pd.DataFrame()

    # Fetch track audio features
    for i in tqdm(range(0, len(track_ids_uni), 25)):
        try:
            track_feature = spotify_client.audio_features(
                track_ids_uni[i:i+25])
            track_df = pd.DataFrame(track_feature)
            audio_features = pd.concat([audio_features, track_df], axis=0)
        except Exception as e:
            print(e)

    # Fetch track details
    for i in tqdm(range(0, len(track_ids_uni), 25)):
        try:
            track_features = spotify_client.tracks(track_ids_uni[i:i+25])
            for x in range(len(track_features['tracks'])):
                track_pop = pd.DataFrame(
                    [track_ids_uni[i+x]], columns=['Track_uri'])
                track_pop['Track_release_date'] = track_features['tracks'][x]['album']['release_date']
                track_pop['Track_pop'] = track_features['tracks'][x]['popularity']
                track_pop['Artist_uri'] = track_features['tracks'][x]['artists'][0]['id']
                track_pop['Album_uri'] = track_features['tracks'][x]['album']['id']
                track_details = pd.concat([track_details, track_pop], axis=0)
        except Exception as e:
            print(e)

    # Fetch artist details
    for i in tqdm(range(0, len(artist_id_uni), 25)):
        try:
            artist_features = spotify_client.artists(artist_id_uni[i:i+25])
            for x in range(len(artist_features['artists'])):
                artist_df = pd.DataFrame(
                    [artist_id_uni[i+x]], columns=['Artist_uri'])
                artist_pop = artist_features['artists'][x]['popularity']
                artist_genres = artist_features['artists'][x]['genres']
                artist_df['Artist_pop'] = artist_pop
                artist_df['genres'] = " ".join(
                    [re.sub(' ', '_', genre) for genre in artist_genres]) if artist_genres else "unknown"
                artist_details = pd.concat([artist_details, artist_df], axis=0)
        except Exception as e:
            print(e)

    return audio_features, track_details, artist_details
