from fetch_track_artist_details import fetch_track_artist_details
from fetch_spotify_recommendations import fetch_spotify_recommendations
from recommend_tracks import recommend_tracks
from preprocess_and_merge_data import preprocess_and_merge_data
from load_and_preprocess_data import load_and_preprocess_data
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

# For Debugging
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Auxiliary functions

##########################################################################################
# Load Spotify Credentials


def load_spotify_credentials(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

##########################################################################################
# Authenticate with Spotify


def local_authenticate_spotify(spotify_credentials):
    # Adjusting to the keys as they appear in the YAML file
    client_id = spotify_credentials.get("Client_id")
    client_secret = spotify_credentials.get("client_secret")

    if not client_id or not client_secret:
        raise ValueError(
            "Spotify credentials must include 'Client_id' and 'client_secret'.")

    auth_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)


##########################################################################################


def get_IDs(spotify_client, playlist_id):
    track_ids = []
    artist_ids = []
    playlist = spotify_client.playlist(playlist_id)

    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
        artist = item['track']['artists']
        artist_ids.append(artist[0]['id'])

    return track_ids, artist_ids


##########################################################################################

# FastAPI configuration
api_title = "CMU Music Recommender"

api_description = """
CMU Music Recommender allows the user to get new music recommendations based on a playlist 
that they have listened to on Spotify. It leverages advanced machine learning techniques to 
analyze user preferences and suggest tracks that align with their musical taste.

If you want to test it out just click on the "Try it out" button below and then Execute.
"""

app = FastAPI(title=api_title, description=api_description)


@app.post("/recommendations/")
async def get_recommendations(playlist_id: str = ""):
    try:
        # Adjusted regular expression to optionally match 'playlist/'
        match = re.search(r'(?:playlist\/)?([\w\d]+)', playlist_id)

        if playlist_id and not match:
            return {"error": "Invalid playlist ID. Please check your playlist ID. It should be in the format like '37i9dQZF1E8NgXcf5gQPXv' or a full Spotify playlist link."}

        # Default playlist ID if none is provided
        default_playlist_id = '37i9dQZF1E8NgXcf5gQPXv'
        playlist_id = match.group(1) if match else default_playlist_id
        playlist_id_full = f'spotify:playlist:{playlist_id}'

        spotify_credentials_file = 'Spotify.yaml'
        spotify_credentials = load_spotify_credentials(
            spotify_credentials_file)
        sp = local_authenticate_spotify(spotify_credentials)

        # logging.debug("Fetching track and artist IDs")
        track_ids, artist_ids = get_IDs(sp, playlist_id_full)
        # logging.debug("Track IDs: %s", track_ids)
        # logging.debug("Artist IDs: %s", artist_ids)

        logging.debug("Fetching track and artist details")
        audio_features, track_details, artist_details = fetch_track_artist_details(
            sp, track_ids, artist_ids)
        logging.debug("Audio Features: %s", audio_features.shape)
        logging.debug("Track Details: %s", track_details.shape)
        logging.debug("Artist Details: %s", artist_details.shape)

        data_file_path = './data/1M_processed.csv'
        df = load_and_preprocess_data(data_file_path)

        # Merge data
        df_update, test = preprocess_and_merge_data(
            df, audio_features, track_details, artist_details)

        # Generate playvec by summing the features of the user's playlist
        playvec = pd.DataFrame(test.sum(axis=0)).T

        # Generate recommendations
        custom_recommendations = recommend_tracks(df_update, playvec, sp)

        # Convert DataFrame to list of dictionaries for JSON serialization
        recommendations = custom_recommendations.to_dict(orient='records')

        # Log recommendations
        logging.debug("Recommendations: %s", custom_recommendations.head())

        return {"playlist_id": playlist_id, "recommendations": recommendations}

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        # Automatically logs the stack trace
        logging.exception("An error occurred")
        raise HTTPException(status_code=500, detail=error_message)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
