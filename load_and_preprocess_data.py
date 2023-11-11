
import pandas as pd


def load_and_preprocess_data(file_path):
    dtypes = {
        'track_uri': 'object', 'artist_uri': 'object', 'album_uri': 'object',
        'danceability': 'float16', 'energy': 'float16', 'key': 'float16',
        'loudness': 'float16', 'mode': 'float16', 'speechiness': 'float16',
        'acousticness': 'float16', 'instrumentalness': 'float16',
        'liveness': 'float16', 'valence': 'float16', 'tempo': 'float16',
        'duration_ms': 'float32', 'time_signature': 'float16',
        'Track_release_date': 'int8', 'Track_pop': 'int8', 'Artist_pop': 'int8',
        'Artist_genres': 'object'
    }
    try:
        df = pd.read_csv(file_path, dtype=dtypes)
    except Exception as e:
        print('Failed to load data:', e)
        df = pd.DataFrame()

    # Add any additional preprocessing steps here if needed
    return df
