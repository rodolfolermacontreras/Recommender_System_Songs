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


def fetch_spotify_recommendations(test, sp):
    Spotifyresult = pd.DataFrame()

    for i in range(len(test) - 1):
        if len(Spotifyresult) >= 20:
            break

        # Fetch recommendations based on a seed of tracks
        ff = sp.recommendations(seed_tracks=list(
            test.track_uri[1 + i:5 + i]), limit=2)

        for z in range(2):
            result = pd.DataFrame([z + (2 * i) + 1], columns=['Index'])
            result['track_name'] = ff['tracks'][z]['name']
            result['artist_name'] = ff['tracks'][z]['artists'][0]['name']
            result['pop'] = ff['tracks'][z]["popularity"]
            Spotifyresult = pd.concat([Spotifyresult, result], axis=0)

    return Spotifyresult.reset_index(drop=True)
