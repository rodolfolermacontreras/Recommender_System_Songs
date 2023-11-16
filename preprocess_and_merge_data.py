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


def preprocess_and_merge_data(df, audio_features, track_details, artist_details):

    # logging.debug("Initial DataFrames:")
    # logging.debug("Track Details Columns: %s", track_details.columns)
    # logging.debug("Artist Details Columns: %s", artist_details.columns)
    # logging.debug("Audio Features Columns: %s", audio_features.columns)
    # logging.debug("Dataframe Columns: %s", df.columns)

    # Ensure 'Artist_uri' column exists in artist_details
    assert 'Artist_uri' in artist_details.columns, "Column 'Artist_uri' not found in artist_details DataFrame"

    # Rename columns
    test = pd.DataFrame(track_details, columns=[
                        'Track_uri', 'Artist_uri', 'Album_uri'])
    test.rename(columns={'Track_uri': 'track_uri',
                'Artist_uri': 'artist_uri', 'Album_uri': 'album_uri'}, inplace=True)
    audio_features_update = audio_features.copy()
    audio_features_update.drop(
        columns=['type', 'uri', 'track_href', 'analysis_url'], axis=1, inplace=True)

    # # Add logging before the problematic merge
    # logging.debug("Merging test DataFrame with artist_details")
    # logging.debug("Test Columns (Before Merge): %s", test.columns)
    # logging.debug("Artist Details Columns (Before Merge): %s",
    #               artist_details.columns)

    test = pd.merge(test, audio_features_update,
                    left_on="track_uri", right_on="id", how='inner')
    test = pd.merge(test, track_details, left_on="track_uri",
                    right_on="Track_uri", how='inner')
    # Perform the merge
    try:
        test = pd.merge(test, artist_details, left_on="artist_uri",
                        right_on="Artist_uri", how='inner')
    except KeyError as e:
        logging.error("KeyError during merge: %s", e)
        raise
    test.drop_duplicates(inplace=True)

    test.rename(columns={'genres': 'Artist_genres'}, inplace=True)
    test.drop(columns=['Track_uri', 'Artist_uri_x',
              'Artist_uri_y', 'Album_uri', 'id'], axis=1, inplace=True)
    test.dropna(axis=0, inplace=True)

    test['Track_pop'] = test['Track_pop'].apply(lambda x: int(x/5))
    test['Artist_pop'] = test['Artist_pop'].apply(lambda x: int(x/5))
    test['Track_release_date'] = test['Track_release_date'].apply(
        lambda x: x.split('-')[0])
    test['Track_release_date'] = test['Track_release_date'].astype('int16')
    test['Track_release_date'] = test['Track_release_date'].apply(
        lambda x: int(x/50))

    test[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']] = test[[
        'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']].astype('float16')
    test[['duration_ms']] = test[['duration_ms']].astype('float32')
    test[['Track_release_date', 'Track_pop', 'Artist_pop']] = test[[
        'Track_release_date', 'Track_pop', 'Artist_pop']].astype('int8')
    currentdf = len(df)

    df = pd.concat([df, test], axis=0)
    # keep last to keep the dataset updated
    df.drop_duplicates(subset=['track_uri'], inplace=True, keep='last')
    df.dropna(axis=0, inplace=True)

    # saving the tracks if they weren't found in the dataset
    if len(df) > currentdf:
        df.to_csv('./data/1M_processed.csv', index=False)
        print('{} New Found'.format(len(df)-currentdf))
        # dropped track with 0 popularity score to save space and ram for the final model
        streamlit = df[df.Track_pop > 0]
        ##### may need to adjust#####
        streamlit.to_csv('./data/streamlit.csv', index=False)
        del streamlit

    df = df[~df['track_uri'].isin(test['track_uri'].values)]
    test['Artist_genres'] = test['Artist_genres'].apply(lambda x: x.split(" "))
    tfidf = TfidfVectorizer(max_features=5)  # max_features=5
    tfidf_matrix = tfidf.fit_transform(
        test['Artist_genres'].apply(lambda x: " ".join(x)))
    genre_df = pd.DataFrame(tfidf_matrix.toarray())
    genre_df.columns = ['genre' + "|" +
                        i for i in tfidf.get_feature_names_out()]

    genre_df = genre_df.astype('float16')
    test.drop(columns=['Artist_genres'], axis=1, inplace=True)
    test = pd.concat([test.reset_index(drop=True),
                     genre_df.reset_index(drop=True)], axis=1)
    test.isna().sum().sum()

    df['Artist_genres'] = df['Artist_genres'].apply(lambda x: x.split(" "))
    tfidf_matrix = tfidf.transform(
        df['Artist_genres'].apply(lambda x: " ".join(x)))
    genre_df = pd.DataFrame(tfidf_matrix.toarray())
    genre_df.columns = ['genre' + "|" +
                        i for i in tfidf.get_feature_names_out()]
    genre_df = genre_df.astype('float16')
    df.drop(columns=['Artist_genres'], axis=1, inplace=True)

    df = pd.concat([df.reset_index(drop=True),
                   genre_df.reset_index(drop=True)], axis=1)
    try:
        df.drop(columns=['genre|unknown'], axis=1, inplace=True)
        test.drop(columns=['genre|unknown'], axis=1, inplace=True)
    except:
        print('genre|unknown not found')

    sc = MinMaxScaler()
    # in the saved dataset get all rows, and columns including audio features. note that genre is not included
    df[df.columns[3:19]] = sc.fit_transform(df.iloc[:, 3:19])
    pickle.dump(sc, open('./data/sc.sav', 'wb'))

    # based on input play list, get all rows, and columns including audio features. note that genre is not included
    test[test.columns[3:19]] = sc.transform(test.iloc[:, 3:19])

    return df, test
