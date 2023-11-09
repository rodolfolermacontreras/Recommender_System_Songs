{
    "cells": [
        {
            "cell_type": "code",
            "source": [
                "pip install spotipy"
            ],
            "metadata": {
                "id": "WCuxcbMHcnf_",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699497593838,
                    "user_tz": 300,
                    "elapsed": 16061,
                    "user": {
                        "displayName": "Junbo Wang",
                        "userId": "14682640775352485098"
                    }
                },
                "outputId": "0dd6e215-a9aa-454c-974d-ac04cd803886"
            },
            "execution_count": 1,
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "Collecting spotipy\n",
                        "  Downloading spotipy-2.23.0-py3-none-any.whl (29 kB)\n",
                        "Collecting redis>=3.5.3 (from spotipy)\n",
                        "  Downloading redis-5.0.1-py3-none-any.whl (250 kB)\n",
                        "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m250.3/250.3 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
                        "\u001b[?25hRequirement already satisfied: requests>=2.25.0 in /usr/local/lib/python3.10/dist-packages (from spotipy) (2.31.0)\n",
                        "Requirement already satisfied: six>=1.15.0 in /usr/local/lib/python3.10/dist-packages (from spotipy) (1.16.0)\n",
                        "Requirement already satisfied: urllib3>=1.26.0 in /usr/local/lib/python3.10/dist-packages (from spotipy) (2.0.7)\n",
                        "Requirement already satisfied: async-timeout>=4.0.2 in /usr/local/lib/python3.10/dist-packages (from redis>=3.5.3->spotipy) (4.0.3)\n",
                        "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.25.0->spotipy) (3.3.2)\n",
                        "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.25.0->spotipy) (3.4)\n",
                        "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.25.0->spotipy) (2023.7.22)\n",
                        "Installing collected packages: redis, spotipy\n",
                        "Successfully installed redis-5.0.1 spotipy-2.23.0\n"
                    ]
                }
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "metadata": {
                "id": "2MiS9YMvckgh",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699497596455,
                    "user_tz": 300,
                    "elapsed": 2622,
                    "user": {
                        "displayName": "Junbo Wang",
                        "userId": "14682640775352485098"
                    }
                }
            },
            "outputs": [],
            "source": [
                "import os\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import json\n",
                "import spotipy\n",
                "import spotipy.oauth2 as oauth2\n",
                "from spotipy.oauth2 import SpotifyOAuth,SpotifyClientCredentials\n",
                "import yaml\n",
                "import re\n",
                "from tqdm import tqdm\n",
                "import multiprocessing as mp\n",
                "import time\n",
                "import random\n",
                "import datetime\n",
                "import pickle\n",
                "from sklearn.feature_extraction.text import TfidfVectorizer\n",
                "from sklearn.metrics.pairwise import cosine_similarity\n",
                "from sklearn.preprocessing import MinMaxScaler\n",
                "import matplotlib.pyplot as plt\n",
                "from skimage import io\n",
                "from sklearn.decomposition import PCA"
            ]
        },
        {
            "cell_type": "code",
            "source": [
                "from google.colab import drive\n",
                "drive.mount('/content/drive')"
            ],
            "metadata": {
                "id": "l32UqYN0copA",
                "colab": {
                    "base_uri": "https://localhost:8080/",
                    "height": 338
                },
                "executionInfo": {
                    "status": "error",
                    "timestamp": 1699497628337,
                    "user_tz": 300,
                    "elapsed": 4667,
                    "user": {
                        "displayName": "Junbo Wang",
                        "userId": "14682640775352485098"
                    }
                },
                "outputId": "2dc440a9-6eca-4355-8d92-2cc99703cd77"
            },
            "execution_count": 5,
            "outputs": [
                {
                    "output_type": "error",
                    "ename": "MessageError",
                    "evalue": "ignored",
                    "traceback": [
                        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
                        "\u001b[0;31mMessageError\u001b[0m                              Traceback (most recent call last)",
                        "\u001b[0;32m<ipython-input-5-d5df0069828e>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolab\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdrive\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mdrive\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmount\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'/content/drive'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
                        "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/drive.py\u001b[0m in \u001b[0;36mmount\u001b[0;34m(mountpoint, force_remount, timeout_ms, readonly)\u001b[0m\n\u001b[1;32m    101\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mmount\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmountpoint\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mforce_remount\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout_ms\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m120000\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreadonly\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    102\u001b[0m   \u001b[0;34m\"\"\"Mount your Google Drive at the specified mountpoint path.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 103\u001b[0;31m   return _mount(\n\u001b[0m\u001b[1;32m    104\u001b[0m       \u001b[0mmountpoint\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    105\u001b[0m       \u001b[0mforce_remount\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mforce_remount\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
                        "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/drive.py\u001b[0m in \u001b[0;36m_mount\u001b[0;34m(mountpoint, force_remount, timeout_ms, ephemeral, readonly)\u001b[0m\n\u001b[1;32m    130\u001b[0m   )\n\u001b[1;32m    131\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mephemeral\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 132\u001b[0;31m     _message.blocking_request(\n\u001b[0m\u001b[1;32m    133\u001b[0m         \u001b[0;34m'request_auth'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m'authType'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m'dfs_ephemeral'\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout_sec\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    134\u001b[0m     )\n",
                        "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/_message.py\u001b[0m in \u001b[0;36mblocking_request\u001b[0;34m(request_type, request, timeout_sec, parent)\u001b[0m\n\u001b[1;32m    174\u001b[0m       \u001b[0mrequest_type\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparent\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparent\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexpect_reply\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    175\u001b[0m   )\n\u001b[0;32m--> 176\u001b[0;31m   \u001b[0;32mreturn\u001b[0m \u001b[0mread_reply_from_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout_sec\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
                        "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/_message.py\u001b[0m in \u001b[0;36mread_reply_from_input\u001b[0;34m(message_id, timeout_sec)\u001b[0m\n\u001b[1;32m    101\u001b[0m     ):\n\u001b[1;32m    102\u001b[0m       \u001b[0;32mif\u001b[0m \u001b[0;34m'error'\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mreply\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 103\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mMessageError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreply\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'error'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    104\u001b[0m       \u001b[0;32mreturn\u001b[0m \u001b[0mreply\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'data'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    105\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
                        "\u001b[0;31mMessageError\u001b[0m: Error: credential propagation was unsuccessful"
                    ]
                }
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "ymDfatMqckgi",
                "executionInfo": {
                    "status": "aborted",
                    "timestamp": 1699497604450,
                    "user_tz": 300,
                    "elapsed": 3,
                    "user": {
                        "displayName": "Junbo Wang",
                        "userId": "14682640775352485098"
                    }
                }
            },
            "outputs": [],
            "source": [
                "# Open the YAML file that contains the Spotify API credentials.\n",
                "stream= open(\"/content/drive/MyDrive/Spotify/Spotify.yaml\")\n",
                "spotify_details = yaml.safe_load(stream)\n",
                "auth_manager = SpotifyClientCredentials(client_id=spotify_details['Client_id'],\n",
                "                                        client_secret=spotify_details['client_secret'])\n",
                "sp = spotipy.client.Spotify(auth_manager=auth_manager)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {
                "id": "j-eh3Pgvckgj"
            },
            "source": [
                "# Importing the dataset"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "XnAdKmqmckgj"
            },
            "outputs": [],
            "source": [
                "dtypes = {'track_uri': 'object', 'artist_uri': 'object', 'album_uri': 'object', 'danceability': 'float16', 'energy': 'float16', 'key': 'float16',\n",
                "               'loudness': 'float16', 'mode': 'float16', 'speechiness': 'float16', 'acousticness': 'float16', 'instrumentalness': 'float16',\n",
                "               'liveness': 'float16', 'valence': 'float16', 'tempo': 'float16', 'duration_ms': 'float32', 'time_signature': 'float16',\n",
                "               'Track_release_date': 'int8', 'Track_pop': 'int8', 'Artist_pop': 'int8', 'Artist_genres': 'object'}\n",
                "try:\n",
                "    df=pd.read_csv('/content/drive/MyDrive/Spotify/data/1M_processed.csv',dtype=dtypes)\n",
                "except:\n",
                "    print('Failed to load grow')\n",
                "    df=pd.read_csv('/content/drive/MyDrive/Spotify/data/1M_processed.csv',dtype=dtypes)\n"
            ]
        },
        {
            "cell_type": "code",
            "source": [
                "df.shape"
            ],
            "metadata": {
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "id": "GlCARpC2Ytaa",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417449946,
                    "user_tz": 300,
                    "elapsed": 11,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                },
                "outputId": "65ed1e44-872a-446a-af3b-983f35908e8a"
            },
            "execution_count": null,
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "(1163321, 20)"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 6
                }
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {
                "id": "bmfaCKRWckgj"
            },
            "source": [
                "# Test"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {
                "id": "JqT55ObUckgj"
            },
            "source": [
                "Extract playlist tracks and artist uri"
            ]
        },
        {
            "cell_type": "code",
            "source": [
                "def get_IDs (playlist_id):\n",
                "    track_ids = []\n",
                "    artist_id = []\n",
                "    playlist=sp.playlist (playlist_id)\n",
                "    for item in playlist['tracks']['items']:\n",
                "        track=item['track']\n",
                "        track_ids.append(track['id'])\n",
                "        artist=item['track']['artists']\n",
                "        artist_id.append(artist[0]['id'])\n",
                "    return track_ids,artist_id"
            ],
            "metadata": {
                "id": "Yf47anptVi8B"
            },
            "execution_count": null,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                " playlist_id = 'spotify:playlist:1VDEf4vANEPRlrXVken86a'\n",
                "\n"
            ],
            "metadata": {
                "id": "BW0IJegvXIRB"
            },
            "execution_count": null,
            "outputs": []
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "7Jp_ykpdckgj",
                "outputId": "ca8a48e6-be75-46f3-a594-4c428313dab2",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417450650,
                    "user_tz": 300,
                    "elapsed": 715,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "100\n",
                        "100\n"
                    ]
                }
            ],
            "source": [
                "track_ids,artist_id = get_IDs (playlist_id)\n",
                "print (len(track_ids))\n",
                "print (len(artist_id))"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {
                "id": "KTUesuANckgk"
            },
            "source": [
                "getting the unique URI and repeating the extraction features and preprocessing steps for the user's playlist (input)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "mjLUwIZmckgk"
            },
            "outputs": [],
            "source": [
                "artist_id_uni=list(set(artist_id))\n",
                "track_ids_uni=list(set(track_ids))"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "oNfEjrQJckgk",
                "outputId": "2b5c4b54-c3f6-4b65-82f7-feb522f0e47e",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417450955,
                    "user_tz": 300,
                    "elapsed": 308,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stderr",
                    "text": [
                        "100%|██████████| 4/4 [00:00<00:00, 12.44it/s]"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "expected string or bytes-like object\n"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stderr",
                    "text": [
                        "\n"
                    ]
                }
            ],
            "source": [
                "audio_features=pd.DataFrame()\n",
                "for i in tqdm(range(0,len(track_ids_uni),25)):\n",
                "    try:\n",
                "     track_feature = sp.audio_features(track_ids_uni[i:i+25])\n",
                "     track_df = pd.DataFrame(track_feature)\n",
                "     audio_features=pd.concat([audio_features,track_df],axis=0)\n",
                "    except Exception as e:\n",
                "        print(e)\n",
                "        continue"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "kJg8SZmuckgk",
                "outputId": "b70cd3ee-daf9-45e6-d385-c5ec30a26373",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417452194,
                    "user_tz": 300,
                    "elapsed": 1242,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stderr",
                    "text": [
                        " 50%|█████     | 2/4 [00:00<00:00,  2.20it/s]"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "expected string or bytes-like object\n"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stderr",
                    "text": [
                        "100%|██████████| 4/4 [00:01<00:00,  2.98it/s]\n"
                    ]
                }
            ],
            "source": [
                "track_=pd.DataFrame()\n",
                "for i in tqdm(range(0,len(track_ids_uni),25)):\n",
                "    try:\n",
                "        track_features = sp.tracks(track_ids_uni[i:i+25])\n",
                "        for x in range(25):\n",
                "            track_pop=pd.DataFrame([track_ids_uni[i+x]],columns=['Track_uri'])\n",
                "            track_pop['Track_release_date']=track_features['tracks'][x]['album']['release_date']\n",
                "            track_pop['Track_pop'] = track_features['tracks'][x][\"popularity\"]\n",
                "            track_pop['Artist_uri']=track_features['tracks'][x]['artists'][0]['id']\n",
                "            track_pop['Album_uri']=track_features['tracks'][x]['album']['id']\n",
                "            track_=pd.concat([track_,track_pop],axis=0)\n",
                "    except Exception as e:\n",
                "        print(e)\n",
                "        continue"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "QKHsSlNIckgk",
                "outputId": "f80dc735-ce52-4ecf-efb2-bfc1cc109658",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417452840,
                    "user_tz": 300,
                    "elapsed": 649,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stderr",
                    "text": [
                        "\r  0%|          | 0/2 [00:00<?, ?it/s]"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "expected string or bytes-like object\n"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stderr",
                    "text": [
                        "100%|██████████| 2/2 [00:00<00:00,  6.69it/s]"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "list index out of range\n"
                    ]
                },
                {
                    "output_type": "stream",
                    "name": "stderr",
                    "text": [
                        "\n"
                    ]
                }
            ],
            "source": [
                "artist_=pd.DataFrame()\n",
                "for i in tqdm(range(0,len(artist_id_uni),25)):\n",
                "    try:\n",
                "        artist_features = sp.artists(artist_id_uni[i:i+25])\n",
                "        for x in range(25):\n",
                "            artist_df=pd.DataFrame([artist_id_uni[i+x]],columns=['Artist_uri'])\n",
                "            artist_pop = artist_features['artists'][x][\"popularity\"]\n",
                "            artist_genres = artist_features['artists'][x][\"genres\"]\n",
                "            artist_df[\"Artist_pop\"] = artist_pop\n",
                "            if artist_genres:\n",
                "                artist_df[\"genres\"] = \" \".join([re.sub(' ','_',i) for i in artist_genres])\n",
                "            else:\n",
                "                artist_df[\"genres\"] = \"unknown\"\n",
                "            artist_=pd.concat([artist_,artist_df],axis=0)\n",
                "    except Exception as e:\n",
                "        print(e)\n",
                "        continue"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "wx_vQAKgckgl"
            },
            "outputs": [],
            "source": [
                "test=pd.DataFrame(track_,columns=['Track_uri','Artist_uri','Album_uri'])"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "4Wss0MUIckgl"
            },
            "outputs": [],
            "source": [
                "test.rename(columns = {'Track_uri':'track_uri','Artist_uri':'artist_uri','Album_uri':'album_uri'}, inplace = True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "ISo0Jyqkckgl"
            },
            "outputs": [],
            "source": [
                "audio_features.drop(columns=['type','uri','track_href','analysis_url'],axis=1,inplace=True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "7ZPN19bAckgl"
            },
            "outputs": [],
            "source": [
                "test = pd.merge(test,audio_features, left_on = \"track_uri\", right_on= \"id\",how = 'outer')\n",
                "test = pd.merge(test,track_, left_on = \"track_uri\", right_on= \"Track_uri\",how = 'outer')\n",
                "test = pd.merge(test,artist_, left_on = \"artist_uri\", right_on= \"Artist_uri\",how = 'outer')"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "hLDTqGCpckgl"
            },
            "outputs": [],
            "source": [
                "del audio_features,track_,artist_"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "bVNSbxd5ckgl"
            },
            "outputs": [],
            "source": [
                "test.rename(columns = {'genres':'Artist_genres'}, inplace = True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "KQoEbF_Uckgl"
            },
            "outputs": [],
            "source": [
                "test.drop(columns=['Track_uri','Artist_uri_x','Artist_uri_y','Album_uri','id'],axis=1,inplace=True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "TX5XotS6ckgl"
            },
            "outputs": [],
            "source": [
                "test.dropna(axis=0,inplace=True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "m4nuGPnuckgl"
            },
            "outputs": [],
            "source": [
                "test['Track_pop'] = test['Track_pop'].apply(lambda x: int(x/5))\n",
                "test['Artist_pop'] = test['Artist_pop'].apply(lambda x: int(x/5))\n",
                "test['Track_release_date'] = test['Track_release_date'].apply(lambda x: x.split('-')[0])\n",
                "test['Track_release_date']=test['Track_release_date'].astype('int16')\n",
                "test['Track_release_date'] = test['Track_release_date'].apply(lambda x: int(x/50))"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "LFGI2-_9ckgm"
            },
            "outputs": [],
            "source": [
                "test[['danceability', 'energy', 'key','loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness','liveness', 'valence', 'tempo', 'time_signature']]=test[['danceability', 'energy', 'key','loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness','liveness', 'valence', 'tempo','time_signature']].astype('float16')\n",
                "test[['duration_ms']]=test[['duration_ms']].astype('float32')\n",
                "test[['Track_release_date', 'Track_pop', 'Artist_pop']]=test[['Track_release_date', 'Track_pop', 'Artist_pop']].astype('int8')"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "o-J3ri9Nckgm",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417453030,
                    "user_tz": 300,
                    "elapsed": 2,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                },
                "outputId": "18f960e9-e31e-4f13-88b8-25dc51e93b48"
            },
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "1163321"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 24
                }
            ],
            "source": [
                "currentdf=len(df)\n",
                "currentdf"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "-aadz7kZckgm"
            },
            "outputs": [],
            "source": [
                "df=pd.concat([df,test],axis=0)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "V-RfHcD6ckgm"
            },
            "outputs": [],
            "source": [
                "df.drop_duplicates(subset=['track_uri'],inplace=True,keep='last') ## keep last to keep the dataset updated"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "w-Au9kRnckgm"
            },
            "outputs": [],
            "source": [
                "df.dropna(axis=0,inplace=True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "pglTcrCPckgm",
                "outputId": "03d19019-5139-4575-f733-e780a6d59903",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417459136,
                    "user_tz": 300,
                    "elapsed": 4,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "12 New Tracks Found\n"
                    ]
                }
            ],
            "source": [
                "print('{} New Tracks Found'.format(len(df)-currentdf))"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "aZoy-7Q1ckgm",
                "outputId": "32c1024f-6ee1-430f-a753-4adfa7dc7ed5",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417521378,
                    "user_tz": 300,
                    "elapsed": 62245,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "12 New Found\n"
                    ]
                }
            ],
            "source": [
                "#saving the tracks if they weren't found in the dataset\n",
                "if len(df)>currentdf:\n",
                "    df.to_csv('/content/drive/MyDrive/Spotify/data/1M_processed.csv',index=False)\n",
                "    print('{} New Found'.format(len(df)-currentdf))\n",
                "    streamlit=df[df.Track_pop >0]             # dropped track with 0 popularity score to save space and ram for the final model\n",
                "    ##### may need to adjust#####\n",
                "    streamlit.to_csv('/content/drive/MyDrive/Spotify/data/streamlit.csv',index=False)\n",
                "    del streamlit"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "Qm-fYohrckgm"
            },
            "outputs": [],
            "source": [
                "df = df[~df['track_uri'].isin(test['track_uri'].values)]"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "ZANByihzckgm"
            },
            "outputs": [],
            "source": [
                "test['Artist_genres'] = test['Artist_genres'].apply(lambda x: x.split(\" \"))\n",
                "tfidf = TfidfVectorizer(max_features=5) #max_features=5\n",
                "tfidf_matrix = tfidf.fit_transform(test['Artist_genres'].apply(lambda x: \" \".join(x)))\n",
                "genre_df = pd.DataFrame(tfidf_matrix.toarray())\n",
                "genre_df.columns = ['genre' + \"|\" + i for i in tfidf.get_feature_names_out()]"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "-_sLBvy3ckgm"
            },
            "outputs": [],
            "source": [
                "genre_df=genre_df.astype('float16')\n",
                "test.drop(columns=['Artist_genres'],axis=1,inplace=True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "KrV3DMrVckgm"
            },
            "outputs": [],
            "source": [
                "test = pd.concat([test.reset_index(drop=True), genre_df.reset_index(drop=True)],axis = 1)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "qasNuZpGckgm",
                "outputId": "1dd7a911-ec4a-4383-b255-a8fbd4863037",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417521783,
                    "user_tz": 300,
                    "elapsed": 4,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "0"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 34
                }
            ],
            "source": [
                "test.isna().sum().sum()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "i4T9eXvackgm"
            },
            "outputs": [],
            "source": [
                "df['Artist_genres'] = df['Artist_genres'].apply(lambda x: x.split(\" \"))\n",
                "tfidf_matrix = tfidf.transform(df['Artist_genres'].apply(lambda x: \" \".join(x)))\n",
                "genre_df = pd.DataFrame(tfidf_matrix.toarray())\n",
                "genre_df.columns = ['genre' + \"|\" + i for i in tfidf.get_feature_names_out()]"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "KzHpHRAxckgo"
            },
            "outputs": [],
            "source": [
                "genre_df=genre_df.astype('float16')\n",
                "df.drop(columns=['Artist_genres'],axis=1,inplace=True)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "P3NGqDwkckgo"
            },
            "outputs": [],
            "source": [
                "df = pd.concat([df.reset_index(drop=True), genre_df.reset_index(drop=True)],axis = 1)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "UObZYDr_ckgq",
                "outputId": "e9ed663e-9f8e-4532-a021-a6a6ecff376f",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417534481,
                    "user_tz": 300,
                    "elapsed": 7,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "genre|unknown not found\n"
                    ]
                }
            ],
            "source": [
                "try:\n",
                "    df.drop(columns=['genre|unknown'],axis=1,inplace=True)\n",
                "    test.drop(columns=['genre|unknown'],axis=1,inplace=True)\n",
                "except:\n",
                "    print('genre|unknown not found')"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "PX6HKXfbckgq",
                "outputId": "9d64a554-8b45-44ff-8123-ef341fe2946a",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417534481,
                    "user_tz": 300,
                    "elapsed": 5,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "Index(['track_uri', 'artist_uri', 'album_uri', 'danceability', 'energy', 'key',\n",
                            "       'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',\n",
                            "       'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',\n",
                            "       'Track_release_date', 'Track_pop', 'Artist_pop', 'genre|cantopop',\n",
                            "       'genre|mainland_chinese_pop', 'genre|mandopop',\n",
                            "       'genre|singaporean_mandopop', 'genre|singaporean_pop'],\n",
                            "      dtype='object')"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 39
                }
            ],
            "source": [
                "test.columns"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "vZWIG3SAckgr",
                "outputId": "bfa38fa7-5110-455e-9dd7-f4c6f6a5a6c0",
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417534481,
                    "user_tz": 300,
                    "elapsed": 4,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "Index(['track_uri', 'artist_uri', 'album_uri', 'danceability', 'energy', 'key',\n",
                            "       'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',\n",
                            "       'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',\n",
                            "       'Track_release_date', 'Track_pop', 'Artist_pop', 'genre|cantopop',\n",
                            "       'genre|mainland_chinese_pop', 'genre|mandopop',\n",
                            "       'genre|singaporean_mandopop', 'genre|singaporean_pop'],\n",
                            "      dtype='object')"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 40
                }
            ],
            "source": [
                "df.columns"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "ppdru1n8ckgr"
            },
            "outputs": [],
            "source": [
                "sc=MinMaxScaler()\n",
                "df[df.columns[3:19]] = sc.fit_transform(df.iloc[:,3:19]) #in the saved dataset get all rows, and columns including audio features. note that genre is not included\n",
                "pickle.dump(sc, open('/content/drive/MyDrive/Spotify/data/sc.sav', 'wb'))\n",
                "\n",
                "#prepare a new data frame call df_new for PCA analysis\n",
                "df_new = df"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "4N0eXpGHckgr"
            },
            "outputs": [],
            "source": [
                "test[test.columns[3:19]] = sc.transform(test.iloc[:,3:19]) #based on input play list, get all rows, and columns including audio features. note that genre is not included\n",
                "\n",
                "#prepare a new data frame call df_new for PCA analysis\n",
                "test_new = test"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "ILZPsJ1Mckgr",
                "outputId": "941d2f4c-5803-42e3-f534-32d76135c48b",
                "colab": {
                    "base_uri": "https://localhost:8080/",
                    "height": 130
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417535078,
                    "user_tz": 300,
                    "elapsed": 5,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "                                           track_uri  \\\n",
                            "0  3QOQ8HlMpJTupsoj5okuof0CvHKdAXglZGyNCtoZ7JCq6L...   \n",
                            "\n",
                            "                                          artist_uri  \\\n",
                            "0  1cg0bYpP5e2DNG0RgK2CMN1cg0bYpP5e2DNG0RgK2CMN1c...   \n",
                            "\n",
                            "                                           album_uri danceability     energy  \\\n",
                            "0  4IlbFUwa4Fd5laEAD3H6lQ7nD96CUbgCyzRHxbftQhpK4I...    18.891136  18.148926   \n",
                            "\n",
                            "         key   loudness  mode speechiness acousticness  ... duration_ms  \\\n",
                            "0  12.454546  30.469963  32.0     1.58082    21.723438  ...    1.685286   \n",
                            "\n",
                            "  time_signature Track_release_date Track_pop Artist_pop genre|cantopop  \\\n",
                            "0      29.799995          37.974998     15.95       19.6       6.539062   \n",
                            "\n",
                            "  genre|mainland_chinese_pop genre|mandopop genre|singaporean_mandopop  \\\n",
                            "0                   6.613281        21.4375                   6.699219   \n",
                            "\n",
                            "  genre|singaporean_pop  \n",
                            "0              6.699219  \n",
                            "\n",
                            "[1 rows x 24 columns]"
                        ],
                        "text/html": [
                            "\n",
                            "  <div id=\"df-ce138631-4df8-422c-aac9-0ccc77b43830\" class=\"colab-df-container\">\n",
                            "    <div>\n",
                            "<style scoped>\n",
                            "    .dataframe tbody tr th:only-of-type {\n",
                            "        vertical-align: middle;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe tbody tr th {\n",
                            "        vertical-align: top;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe thead th {\n",
                            "        text-align: right;\n",
                            "    }\n",
                            "</style>\n",
                            "<table border=\"1\" class=\"dataframe\">\n",
                            "  <thead>\n",
                            "    <tr style=\"text-align: right;\">\n",
                            "      <th></th>\n",
                            "      <th>track_uri</th>\n",
                            "      <th>artist_uri</th>\n",
                            "      <th>album_uri</th>\n",
                            "      <th>danceability</th>\n",
                            "      <th>energy</th>\n",
                            "      <th>key</th>\n",
                            "      <th>loudness</th>\n",
                            "      <th>mode</th>\n",
                            "      <th>speechiness</th>\n",
                            "      <th>acousticness</th>\n",
                            "      <th>...</th>\n",
                            "      <th>duration_ms</th>\n",
                            "      <th>time_signature</th>\n",
                            "      <th>Track_release_date</th>\n",
                            "      <th>Track_pop</th>\n",
                            "      <th>Artist_pop</th>\n",
                            "      <th>genre|cantopop</th>\n",
                            "      <th>genre|mainland_chinese_pop</th>\n",
                            "      <th>genre|mandopop</th>\n",
                            "      <th>genre|singaporean_mandopop</th>\n",
                            "      <th>genre|singaporean_pop</th>\n",
                            "    </tr>\n",
                            "  </thead>\n",
                            "  <tbody>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>3QOQ8HlMpJTupsoj5okuof0CvHKdAXglZGyNCtoZ7JCq6L...</td>\n",
                            "      <td>1cg0bYpP5e2DNG0RgK2CMN1cg0bYpP5e2DNG0RgK2CMN1c...</td>\n",
                            "      <td>4IlbFUwa4Fd5laEAD3H6lQ7nD96CUbgCyzRHxbftQhpK4I...</td>\n",
                            "      <td>18.891136</td>\n",
                            "      <td>18.148926</td>\n",
                            "      <td>12.454546</td>\n",
                            "      <td>30.469963</td>\n",
                            "      <td>32.0</td>\n",
                            "      <td>1.58082</td>\n",
                            "      <td>21.723438</td>\n",
                            "      <td>...</td>\n",
                            "      <td>1.685286</td>\n",
                            "      <td>29.799995</td>\n",
                            "      <td>37.974998</td>\n",
                            "      <td>15.95</td>\n",
                            "      <td>19.6</td>\n",
                            "      <td>6.539062</td>\n",
                            "      <td>6.613281</td>\n",
                            "      <td>21.4375</td>\n",
                            "      <td>6.699219</td>\n",
                            "      <td>6.699219</td>\n",
                            "    </tr>\n",
                            "  </tbody>\n",
                            "</table>\n",
                            "<p>1 rows × 24 columns</p>\n",
                            "</div>\n",
                            "    <div class=\"colab-df-buttons\">\n",
                            "\n",
                            "  <div class=\"colab-df-container\">\n",
                            "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ce138631-4df8-422c-aac9-0ccc77b43830')\"\n",
                            "            title=\"Convert this dataframe to an interactive table.\"\n",
                            "            style=\"display:none;\">\n",
                            "\n",
                            "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
                            "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
                            "  </svg>\n",
                            "    </button>\n",
                            "\n",
                            "  <style>\n",
                            "    .colab-df-container {\n",
                            "      display:flex;\n",
                            "      gap: 12px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert {\n",
                            "      background-color: #E8F0FE;\n",
                            "      border: none;\n",
                            "      border-radius: 50%;\n",
                            "      cursor: pointer;\n",
                            "      display: none;\n",
                            "      fill: #1967D2;\n",
                            "      height: 32px;\n",
                            "      padding: 0 0 0 0;\n",
                            "      width: 32px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert:hover {\n",
                            "      background-color: #E2EBFA;\n",
                            "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
                            "      fill: #174EA6;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-buttons div {\n",
                            "      margin-bottom: 4px;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert {\n",
                            "      background-color: #3B4455;\n",
                            "      fill: #D2E3FC;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert:hover {\n",
                            "      background-color: #434B5C;\n",
                            "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
                            "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
                            "      fill: #FFFFFF;\n",
                            "    }\n",
                            "  </style>\n",
                            "\n",
                            "    <script>\n",
                            "      const buttonEl =\n",
                            "        document.querySelector('#df-ce138631-4df8-422c-aac9-0ccc77b43830 button.colab-df-convert');\n",
                            "      buttonEl.style.display =\n",
                            "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
                            "\n",
                            "      async function convertToInteractive(key) {\n",
                            "        const element = document.querySelector('#df-ce138631-4df8-422c-aac9-0ccc77b43830');\n",
                            "        const dataTable =\n",
                            "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
                            "                                                    [key], {});\n",
                            "        if (!dataTable) return;\n",
                            "\n",
                            "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
                            "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
                            "          + ' to learn more about interactive tables.';\n",
                            "        element.innerHTML = '';\n",
                            "        dataTable['output_type'] = 'display_data';\n",
                            "        await google.colab.output.renderOutput(dataTable, element);\n",
                            "        const docLink = document.createElement('div');\n",
                            "        docLink.innerHTML = docLinkHtml;\n",
                            "        element.appendChild(docLink);\n",
                            "      }\n",
                            "    </script>\n",
                            "  </div>\n",
                            "\n",
                            "    </div>\n",
                            "  </div>\n"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 43
                }
            ],
            "source": [
                "playvec=pd.DataFrame(test.sum(axis=0)).T\n",
                "playvec"
            ]
        },
        {
            "cell_type": "code",
            "source": [
                "df['sim']=cosine_similarity(df.drop(['track_uri', 'artist_uri', 'album_uri'], axis = 1),playvec.drop(['track_uri', 'artist_uri', 'album_uri'], axis = 1)) #find cosine similarity between dataset and playlist in general\n",
                "df['sim2']=cosine_similarity(df.iloc[:,16:-1],playvec.iloc[:,16:])  #find cosine similarity between dataset and playlist in terms of track & artist genres\n",
                "df['sim3']=cosine_similarity(df.iloc[:,19:-2],playvec.iloc[:,19:])  #find cosine similarity between dataset and playlist in terms of genres\n",
                "df['sim4']=(df['sim']+df['sim2'])/2\n",
                "#sort based on similarity score, high correlated genres will be pioritzed, then artist & track popularity and audio features\n",
                "df = df.sort_values(['sim3','sim4'],ascending = False,kind='stable')\n",
                "\n",
                "#get the list of track uris, we are output 20 tracks\n",
                "qq=df.groupby('artist_uri').head(2).track_uri.head(20)     #to limit recmmendation by same artist\n",
                "\n",
                "#get recommendation track detail\n",
                "aa=sp.tracks(qq[0:20])\n",
                "Fresult=pd.DataFrame()\n",
                "for i in range(20):\n",
                "    result=pd.DataFrame([i])\n",
                "    result['track_name']=aa['tracks'][i]['name']\n",
                "    result['artist_name']=aa['tracks'][i]['artists'][0]['name']\n",
                "    #result['url']=aa['tracks'][i]['external_urls']['spotify']\n",
                "    result['pop'] = aa['tracks'][i][\"popularity\"]\n",
                "    #result['image']=aa['tracks'][i]['album']['images'][1]['url']\n",
                "    Fresult=pd.concat([Fresult,result],axis=0)\n",
                "Fresult"
            ],
            "metadata": {
                "colab": {
                    "base_uri": "https://localhost:8080/",
                    "height": 677
                },
                "id": "nmQnqq4MnhOd",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417542549,
                    "user_tz": 300,
                    "elapsed": 7475,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                },
                "outputId": "28146117-a06f-43c1-be29-c7efa81a48d7"
            },
            "execution_count": null,
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "    0   track_name  artist_name  pop\n",
                            "0   0          慢慢等      WeiBird   58\n",
                            "0   1          還是會      WeiBird   55\n",
                            "0   2          帶我走  Rainie Yang   55\n",
                            "0   3           暗號     Jay Chou   55\n",
                            "0   4      愛 請問怎麼走        A-Lin   46\n",
                            "0   5           擱淺     Jay Chou   66\n",
                            "0   6  那是你離開了北京的生活    Joker Xue   45\n",
                            "0   7       以後別做朋友    Eric Chou   64\n",
                            "0   8          木偶人    Joker Xue   43\n",
                            "0   9     一個人想著一個人   Pets Tseng   56\n",
                            "0  10          年輪說  Rainie Yang   58\n",
                            "0  11           22    David Tao   49\n",
                            "0  12          喜歡你     LaLa Hsu   49\n",
                            "0  13           寧夏   Fish Leong   48\n",
                            "0  14          跟你住      Shi Shi   48\n",
                            "0  15         分手快樂   Fish Leong   52\n",
                            "0  16        還是要幸福    Hebe Tien   49\n",
                            "0  17           不哭   Cyndi Wang    0\n",
                            "0  18         寂寞不痛        A-Lin   43\n",
                            "0  19        愛的就是你  Leehom Wang   45"
                        ],
                        "text/html": [
                            "\n",
                            "  <div id=\"df-4472fb7f-2201-4174-9d03-a0a9aa65dd42\" class=\"colab-df-container\">\n",
                            "    <div>\n",
                            "<style scoped>\n",
                            "    .dataframe tbody tr th:only-of-type {\n",
                            "        vertical-align: middle;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe tbody tr th {\n",
                            "        vertical-align: top;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe thead th {\n",
                            "        text-align: right;\n",
                            "    }\n",
                            "</style>\n",
                            "<table border=\"1\" class=\"dataframe\">\n",
                            "  <thead>\n",
                            "    <tr style=\"text-align: right;\">\n",
                            "      <th></th>\n",
                            "      <th>0</th>\n",
                            "      <th>track_name</th>\n",
                            "      <th>artist_name</th>\n",
                            "      <th>pop</th>\n",
                            "    </tr>\n",
                            "  </thead>\n",
                            "  <tbody>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>0</td>\n",
                            "      <td>慢慢等</td>\n",
                            "      <td>WeiBird</td>\n",
                            "      <td>58</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>1</td>\n",
                            "      <td>還是會</td>\n",
                            "      <td>WeiBird</td>\n",
                            "      <td>55</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>2</td>\n",
                            "      <td>帶我走</td>\n",
                            "      <td>Rainie Yang</td>\n",
                            "      <td>55</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>3</td>\n",
                            "      <td>暗號</td>\n",
                            "      <td>Jay Chou</td>\n",
                            "      <td>55</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>4</td>\n",
                            "      <td>愛 請問怎麼走</td>\n",
                            "      <td>A-Lin</td>\n",
                            "      <td>46</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>5</td>\n",
                            "      <td>擱淺</td>\n",
                            "      <td>Jay Chou</td>\n",
                            "      <td>66</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>6</td>\n",
                            "      <td>那是你離開了北京的生活</td>\n",
                            "      <td>Joker Xue</td>\n",
                            "      <td>45</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>7</td>\n",
                            "      <td>以後別做朋友</td>\n",
                            "      <td>Eric Chou</td>\n",
                            "      <td>64</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>8</td>\n",
                            "      <td>木偶人</td>\n",
                            "      <td>Joker Xue</td>\n",
                            "      <td>43</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>9</td>\n",
                            "      <td>一個人想著一個人</td>\n",
                            "      <td>Pets Tseng</td>\n",
                            "      <td>56</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>10</td>\n",
                            "      <td>年輪說</td>\n",
                            "      <td>Rainie Yang</td>\n",
                            "      <td>58</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>11</td>\n",
                            "      <td>22</td>\n",
                            "      <td>David Tao</td>\n",
                            "      <td>49</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>12</td>\n",
                            "      <td>喜歡你</td>\n",
                            "      <td>LaLa Hsu</td>\n",
                            "      <td>49</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>13</td>\n",
                            "      <td>寧夏</td>\n",
                            "      <td>Fish Leong</td>\n",
                            "      <td>48</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>14</td>\n",
                            "      <td>跟你住</td>\n",
                            "      <td>Shi Shi</td>\n",
                            "      <td>48</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>15</td>\n",
                            "      <td>分手快樂</td>\n",
                            "      <td>Fish Leong</td>\n",
                            "      <td>52</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>16</td>\n",
                            "      <td>還是要幸福</td>\n",
                            "      <td>Hebe Tien</td>\n",
                            "      <td>49</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>17</td>\n",
                            "      <td>不哭</td>\n",
                            "      <td>Cyndi Wang</td>\n",
                            "      <td>0</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>18</td>\n",
                            "      <td>寂寞不痛</td>\n",
                            "      <td>A-Lin</td>\n",
                            "      <td>43</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>19</td>\n",
                            "      <td>愛的就是你</td>\n",
                            "      <td>Leehom Wang</td>\n",
                            "      <td>45</td>\n",
                            "    </tr>\n",
                            "  </tbody>\n",
                            "</table>\n",
                            "</div>\n",
                            "    <div class=\"colab-df-buttons\">\n",
                            "\n",
                            "  <div class=\"colab-df-container\">\n",
                            "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4472fb7f-2201-4174-9d03-a0a9aa65dd42')\"\n",
                            "            title=\"Convert this dataframe to an interactive table.\"\n",
                            "            style=\"display:none;\">\n",
                            "\n",
                            "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
                            "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
                            "  </svg>\n",
                            "    </button>\n",
                            "\n",
                            "  <style>\n",
                            "    .colab-df-container {\n",
                            "      display:flex;\n",
                            "      gap: 12px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert {\n",
                            "      background-color: #E8F0FE;\n",
                            "      border: none;\n",
                            "      border-radius: 50%;\n",
                            "      cursor: pointer;\n",
                            "      display: none;\n",
                            "      fill: #1967D2;\n",
                            "      height: 32px;\n",
                            "      padding: 0 0 0 0;\n",
                            "      width: 32px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert:hover {\n",
                            "      background-color: #E2EBFA;\n",
                            "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
                            "      fill: #174EA6;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-buttons div {\n",
                            "      margin-bottom: 4px;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert {\n",
                            "      background-color: #3B4455;\n",
                            "      fill: #D2E3FC;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert:hover {\n",
                            "      background-color: #434B5C;\n",
                            "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
                            "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
                            "      fill: #FFFFFF;\n",
                            "    }\n",
                            "  </style>\n",
                            "\n",
                            "    <script>\n",
                            "      const buttonEl =\n",
                            "        document.querySelector('#df-4472fb7f-2201-4174-9d03-a0a9aa65dd42 button.colab-df-convert');\n",
                            "      buttonEl.style.display =\n",
                            "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
                            "\n",
                            "      async function convertToInteractive(key) {\n",
                            "        const element = document.querySelector('#df-4472fb7f-2201-4174-9d03-a0a9aa65dd42');\n",
                            "        const dataTable =\n",
                            "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
                            "                                                    [key], {});\n",
                            "        if (!dataTable) return;\n",
                            "\n",
                            "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
                            "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
                            "          + ' to learn more about interactive tables.';\n",
                            "        element.innerHTML = '';\n",
                            "        dataTable['output_type'] = 'display_data';\n",
                            "        await google.colab.output.renderOutput(dataTable, element);\n",
                            "        const docLink = document.createElement('div');\n",
                            "        docLink.innerHTML = docLinkHtml;\n",
                            "        element.appendChild(docLink);\n",
                            "      }\n",
                            "    </script>\n",
                            "  </div>\n",
                            "\n",
                            "\n",
                            "<div id=\"df-37c1e1d7-d517-48de-90ae-c244045ffd73\">\n",
                            "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-37c1e1d7-d517-48de-90ae-c244045ffd73')\"\n",
                            "            title=\"Suggest charts\"\n",
                            "            style=\"display:none;\">\n",
                            "\n",
                            "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
                            "     width=\"24px\">\n",
                            "    <g>\n",
                            "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
                            "    </g>\n",
                            "</svg>\n",
                            "  </button>\n",
                            "\n",
                            "<style>\n",
                            "  .colab-df-quickchart {\n",
                            "      --bg-color: #E8F0FE;\n",
                            "      --fill-color: #1967D2;\n",
                            "      --hover-bg-color: #E2EBFA;\n",
                            "      --hover-fill-color: #174EA6;\n",
                            "      --disabled-fill-color: #AAA;\n",
                            "      --disabled-bg-color: #DDD;\n",
                            "  }\n",
                            "\n",
                            "  [theme=dark] .colab-df-quickchart {\n",
                            "      --bg-color: #3B4455;\n",
                            "      --fill-color: #D2E3FC;\n",
                            "      --hover-bg-color: #434B5C;\n",
                            "      --hover-fill-color: #FFFFFF;\n",
                            "      --disabled-bg-color: #3B4455;\n",
                            "      --disabled-fill-color: #666;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart {\n",
                            "    background-color: var(--bg-color);\n",
                            "    border: none;\n",
                            "    border-radius: 50%;\n",
                            "    cursor: pointer;\n",
                            "    display: none;\n",
                            "    fill: var(--fill-color);\n",
                            "    height: 32px;\n",
                            "    padding: 0;\n",
                            "    width: 32px;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart:hover {\n",
                            "    background-color: var(--hover-bg-color);\n",
                            "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
                            "    fill: var(--button-hover-fill-color);\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart-complete:disabled,\n",
                            "  .colab-df-quickchart-complete:disabled:hover {\n",
                            "    background-color: var(--disabled-bg-color);\n",
                            "    fill: var(--disabled-fill-color);\n",
                            "    box-shadow: none;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-spinner {\n",
                            "    border: 2px solid var(--fill-color);\n",
                            "    border-color: transparent;\n",
                            "    border-bottom-color: var(--fill-color);\n",
                            "    animation:\n",
                            "      spin 1s steps(1) infinite;\n",
                            "  }\n",
                            "\n",
                            "  @keyframes spin {\n",
                            "    0% {\n",
                            "      border-color: transparent;\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "      border-left-color: var(--fill-color);\n",
                            "    }\n",
                            "    20% {\n",
                            "      border-color: transparent;\n",
                            "      border-left-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "    }\n",
                            "    30% {\n",
                            "      border-color: transparent;\n",
                            "      border-left-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "      border-right-color: var(--fill-color);\n",
                            "    }\n",
                            "    40% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "    }\n",
                            "    60% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "    }\n",
                            "    80% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "    }\n",
                            "    90% {\n",
                            "      border-color: transparent;\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "    }\n",
                            "  }\n",
                            "</style>\n",
                            "\n",
                            "  <script>\n",
                            "    async function quickchart(key) {\n",
                            "      const quickchartButtonEl =\n",
                            "        document.querySelector('#' + key + ' button');\n",
                            "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
                            "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
                            "      try {\n",
                            "        const charts = await google.colab.kernel.invokeFunction(\n",
                            "            'suggestCharts', [key], {});\n",
                            "      } catch (error) {\n",
                            "        console.error('Error during call to suggestCharts:', error);\n",
                            "      }\n",
                            "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
                            "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
                            "    }\n",
                            "    (() => {\n",
                            "      let quickchartButtonEl =\n",
                            "        document.querySelector('#df-37c1e1d7-d517-48de-90ae-c244045ffd73 button');\n",
                            "      quickchartButtonEl.style.display =\n",
                            "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
                            "    })();\n",
                            "  </script>\n",
                            "</div>\n",
                            "    </div>\n",
                            "  </div>\n"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 44
                }
            ]
        },
        {
            "cell_type": "code",
            "source": [
                "#### Revision here\n",
                "\n",
                "# Select the numeric features\n",
                "numeric_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',\n",
                "                    'duration_ms', 'time_signature', 'Track_release_date', 'Track_pop', 'Artist_pop']\n",
                "\n",
                "# Extract the numeric features for PCA\n",
                "df_new_numeric = df_new[numeric_features]\n",
                "playvec_new_numeric = playvec[numeric_features]\n",
                "\n",
                "# Initialize PCA, keep 95% of the variance and Fit PCA on the numeric features\n",
                "pca = PCA(n_components=0.95)\n",
                "pca.fit(df_new_numeric)\n",
                "\n",
                "# Transform both df and df_test numeric features\n",
                "df_pca = pca.transform(df_new_numeric)\n",
                "playvec_pca = pca.transform(playvec_new_numeric)\n",
                "\n",
                "# Convert the PCA components into a DataFrame\n",
                "df_pca_df = pd.DataFrame(df_pca, index=df_new.index)\n",
                "playvec_pca_df = pd.DataFrame(playvec_pca, index=playvec.index)"
            ],
            "metadata": {
                "id": "VYb2nStZ8e3t"
            },
            "execution_count": null,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                "#### Find cosine similairty based on PCA model\n",
                "df_new['sim_pca'] = cosine_similarity(df_pca_df, playvec_pca_df) # Calculate the cosine similarity\n",
                "df_new['sim_genres'] = cosine_similarity(df_new.loc[:, df_new.columns.str.startswith('genre')], playvec.loc[:, playvec.columns.str.startswith('genre')]) # Calculate the cosine similarity for genres\n",
                "df_new['sim_combined'] = (df_new['sim_pca'] + df_new['sim_genres']) / 2  # Combine PCA similarity with genre similarity to get a combined similarity score\n",
                "\n",
                "#sort based on similarity score, but give more weight/focus on genre first then PCA\n",
                "df_new = df_new.sort_values(['sim_genres', 'sim_combined'], ascending = False, kind='stable')\n",
                "\n",
                "#get the list of track uris\n",
                "qq=df_new.groupby('artist_uri').head(2).track_uri.head(20)\n",
                "\n",
                "#get recommendation track detail\n",
                "aa=sp.tracks(qq[0:20])\n",
                "Fresult=pd.DataFrame()\n",
                "for i in range(20):\n",
                "    result=pd.DataFrame([i])\n",
                "    result['track_name']=aa['tracks'][i]['name']\n",
                "    result['artist_name']=aa['tracks'][i]['artists'][0]['name']\n",
                "    #result['url']=aa['tracks'][i]['external_urls']['spotify']\n",
                "    result['pop'] = aa['tracks'][i][\"popularity\"]\n",
                "    #result['image']=aa['tracks'][i]['album']['images'][1]['url']\n",
                "    Fresult=pd.concat([Fresult,result],axis=0)\n",
                "Fresult"
            ],
            "metadata": {
                "colab": {
                    "base_uri": "https://localhost:8080/",
                    "height": 677
                },
                "id": "HkG6njZADo9K",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417548789,
                    "user_tz": 300,
                    "elapsed": 4845,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                },
                "outputId": "559ae8d8-53c8-4554-e49c-cccfdc928afb"
            },
            "execution_count": null,
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "    0                track_name     artist_name  pop\n",
                            "0   0                        過程       Soft Lipa   45\n",
                            "0   1                      瘋狂世界          Mayday   36\n",
                            "0   2                      夜間漫遊       Soft Lipa   26\n",
                            "0   3                     我會想念妳  Zhang Zhen Yue   29\n",
                            "0   4                      嫁給我吧             玖壹壹   35\n",
                            "0   5                      辛德瑞拉       Penny Tai   28\n",
                            "0   6                        再見  Zhang Zhen Yue   53\n",
                            "0   7                        不哭      Cyndi Wang    0\n",
                            "0   8                       就是愛      Jolin Tsai   37\n",
                            "0   9                       單眼皮     Rainie Yang   22\n",
                            "0  10                     愛在西元前        Jay Chou   27\n",
                            "0  11                       生煎包         頑童Mj116   39\n",
                            "0  12               Only Lonely           S.H.E   21\n",
                            "0  13                     明天再擱來             玖壹壹   47\n",
                            "0  14                    擁抱你的微笑      Claire Kuo   28\n",
                            "0  15                      那個女孩       David Tao   43\n",
                            "0  16                       任意門     Rainie Yang   31\n",
                            "0  17                       好東西      Jolin Tsai   21\n",
                            "0  18                   把最甜的都給妳         G.U.T.S   38\n",
                            "0  19  輕熟女27 - Acoustic Version       MC HotDog   18"
                        ],
                        "text/html": [
                            "\n",
                            "  <div id=\"df-30ec4699-7391-4e28-8721-f18b1dc11c49\" class=\"colab-df-container\">\n",
                            "    <div>\n",
                            "<style scoped>\n",
                            "    .dataframe tbody tr th:only-of-type {\n",
                            "        vertical-align: middle;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe tbody tr th {\n",
                            "        vertical-align: top;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe thead th {\n",
                            "        text-align: right;\n",
                            "    }\n",
                            "</style>\n",
                            "<table border=\"1\" class=\"dataframe\">\n",
                            "  <thead>\n",
                            "    <tr style=\"text-align: right;\">\n",
                            "      <th></th>\n",
                            "      <th>0</th>\n",
                            "      <th>track_name</th>\n",
                            "      <th>artist_name</th>\n",
                            "      <th>pop</th>\n",
                            "    </tr>\n",
                            "  </thead>\n",
                            "  <tbody>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>0</td>\n",
                            "      <td>過程</td>\n",
                            "      <td>Soft Lipa</td>\n",
                            "      <td>45</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>1</td>\n",
                            "      <td>瘋狂世界</td>\n",
                            "      <td>Mayday</td>\n",
                            "      <td>36</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>2</td>\n",
                            "      <td>夜間漫遊</td>\n",
                            "      <td>Soft Lipa</td>\n",
                            "      <td>26</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>3</td>\n",
                            "      <td>我會想念妳</td>\n",
                            "      <td>Zhang Zhen Yue</td>\n",
                            "      <td>29</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>4</td>\n",
                            "      <td>嫁給我吧</td>\n",
                            "      <td>玖壹壹</td>\n",
                            "      <td>35</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>5</td>\n",
                            "      <td>辛德瑞拉</td>\n",
                            "      <td>Penny Tai</td>\n",
                            "      <td>28</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>6</td>\n",
                            "      <td>再見</td>\n",
                            "      <td>Zhang Zhen Yue</td>\n",
                            "      <td>53</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>7</td>\n",
                            "      <td>不哭</td>\n",
                            "      <td>Cyndi Wang</td>\n",
                            "      <td>0</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>8</td>\n",
                            "      <td>就是愛</td>\n",
                            "      <td>Jolin Tsai</td>\n",
                            "      <td>37</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>9</td>\n",
                            "      <td>單眼皮</td>\n",
                            "      <td>Rainie Yang</td>\n",
                            "      <td>22</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>10</td>\n",
                            "      <td>愛在西元前</td>\n",
                            "      <td>Jay Chou</td>\n",
                            "      <td>27</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>11</td>\n",
                            "      <td>生煎包</td>\n",
                            "      <td>頑童Mj116</td>\n",
                            "      <td>39</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>12</td>\n",
                            "      <td>Only Lonely</td>\n",
                            "      <td>S.H.E</td>\n",
                            "      <td>21</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>13</td>\n",
                            "      <td>明天再擱來</td>\n",
                            "      <td>玖壹壹</td>\n",
                            "      <td>47</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>14</td>\n",
                            "      <td>擁抱你的微笑</td>\n",
                            "      <td>Claire Kuo</td>\n",
                            "      <td>28</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>15</td>\n",
                            "      <td>那個女孩</td>\n",
                            "      <td>David Tao</td>\n",
                            "      <td>43</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>16</td>\n",
                            "      <td>任意門</td>\n",
                            "      <td>Rainie Yang</td>\n",
                            "      <td>31</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>17</td>\n",
                            "      <td>好東西</td>\n",
                            "      <td>Jolin Tsai</td>\n",
                            "      <td>21</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>18</td>\n",
                            "      <td>把最甜的都給妳</td>\n",
                            "      <td>G.U.T.S</td>\n",
                            "      <td>38</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>19</td>\n",
                            "      <td>輕熟女27 - Acoustic Version</td>\n",
                            "      <td>MC HotDog</td>\n",
                            "      <td>18</td>\n",
                            "    </tr>\n",
                            "  </tbody>\n",
                            "</table>\n",
                            "</div>\n",
                            "    <div class=\"colab-df-buttons\">\n",
                            "\n",
                            "  <div class=\"colab-df-container\">\n",
                            "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-30ec4699-7391-4e28-8721-f18b1dc11c49')\"\n",
                            "            title=\"Convert this dataframe to an interactive table.\"\n",
                            "            style=\"display:none;\">\n",
                            "\n",
                            "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
                            "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
                            "  </svg>\n",
                            "    </button>\n",
                            "\n",
                            "  <style>\n",
                            "    .colab-df-container {\n",
                            "      display:flex;\n",
                            "      gap: 12px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert {\n",
                            "      background-color: #E8F0FE;\n",
                            "      border: none;\n",
                            "      border-radius: 50%;\n",
                            "      cursor: pointer;\n",
                            "      display: none;\n",
                            "      fill: #1967D2;\n",
                            "      height: 32px;\n",
                            "      padding: 0 0 0 0;\n",
                            "      width: 32px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert:hover {\n",
                            "      background-color: #E2EBFA;\n",
                            "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
                            "      fill: #174EA6;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-buttons div {\n",
                            "      margin-bottom: 4px;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert {\n",
                            "      background-color: #3B4455;\n",
                            "      fill: #D2E3FC;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert:hover {\n",
                            "      background-color: #434B5C;\n",
                            "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
                            "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
                            "      fill: #FFFFFF;\n",
                            "    }\n",
                            "  </style>\n",
                            "\n",
                            "    <script>\n",
                            "      const buttonEl =\n",
                            "        document.querySelector('#df-30ec4699-7391-4e28-8721-f18b1dc11c49 button.colab-df-convert');\n",
                            "      buttonEl.style.display =\n",
                            "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
                            "\n",
                            "      async function convertToInteractive(key) {\n",
                            "        const element = document.querySelector('#df-30ec4699-7391-4e28-8721-f18b1dc11c49');\n",
                            "        const dataTable =\n",
                            "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
                            "                                                    [key], {});\n",
                            "        if (!dataTable) return;\n",
                            "\n",
                            "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
                            "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
                            "          + ' to learn more about interactive tables.';\n",
                            "        element.innerHTML = '';\n",
                            "        dataTable['output_type'] = 'display_data';\n",
                            "        await google.colab.output.renderOutput(dataTable, element);\n",
                            "        const docLink = document.createElement('div');\n",
                            "        docLink.innerHTML = docLinkHtml;\n",
                            "        element.appendChild(docLink);\n",
                            "      }\n",
                            "    </script>\n",
                            "  </div>\n",
                            "\n",
                            "\n",
                            "<div id=\"df-c5376dec-77a9-4769-92d4-32d9bf6f36fb\">\n",
                            "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c5376dec-77a9-4769-92d4-32d9bf6f36fb')\"\n",
                            "            title=\"Suggest charts\"\n",
                            "            style=\"display:none;\">\n",
                            "\n",
                            "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
                            "     width=\"24px\">\n",
                            "    <g>\n",
                            "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
                            "    </g>\n",
                            "</svg>\n",
                            "  </button>\n",
                            "\n",
                            "<style>\n",
                            "  .colab-df-quickchart {\n",
                            "      --bg-color: #E8F0FE;\n",
                            "      --fill-color: #1967D2;\n",
                            "      --hover-bg-color: #E2EBFA;\n",
                            "      --hover-fill-color: #174EA6;\n",
                            "      --disabled-fill-color: #AAA;\n",
                            "      --disabled-bg-color: #DDD;\n",
                            "  }\n",
                            "\n",
                            "  [theme=dark] .colab-df-quickchart {\n",
                            "      --bg-color: #3B4455;\n",
                            "      --fill-color: #D2E3FC;\n",
                            "      --hover-bg-color: #434B5C;\n",
                            "      --hover-fill-color: #FFFFFF;\n",
                            "      --disabled-bg-color: #3B4455;\n",
                            "      --disabled-fill-color: #666;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart {\n",
                            "    background-color: var(--bg-color);\n",
                            "    border: none;\n",
                            "    border-radius: 50%;\n",
                            "    cursor: pointer;\n",
                            "    display: none;\n",
                            "    fill: var(--fill-color);\n",
                            "    height: 32px;\n",
                            "    padding: 0;\n",
                            "    width: 32px;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart:hover {\n",
                            "    background-color: var(--hover-bg-color);\n",
                            "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
                            "    fill: var(--button-hover-fill-color);\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart-complete:disabled,\n",
                            "  .colab-df-quickchart-complete:disabled:hover {\n",
                            "    background-color: var(--disabled-bg-color);\n",
                            "    fill: var(--disabled-fill-color);\n",
                            "    box-shadow: none;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-spinner {\n",
                            "    border: 2px solid var(--fill-color);\n",
                            "    border-color: transparent;\n",
                            "    border-bottom-color: var(--fill-color);\n",
                            "    animation:\n",
                            "      spin 1s steps(1) infinite;\n",
                            "  }\n",
                            "\n",
                            "  @keyframes spin {\n",
                            "    0% {\n",
                            "      border-color: transparent;\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "      border-left-color: var(--fill-color);\n",
                            "    }\n",
                            "    20% {\n",
                            "      border-color: transparent;\n",
                            "      border-left-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "    }\n",
                            "    30% {\n",
                            "      border-color: transparent;\n",
                            "      border-left-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "      border-right-color: var(--fill-color);\n",
                            "    }\n",
                            "    40% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "    }\n",
                            "    60% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "    }\n",
                            "    80% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "    }\n",
                            "    90% {\n",
                            "      border-color: transparent;\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "    }\n",
                            "  }\n",
                            "</style>\n",
                            "\n",
                            "  <script>\n",
                            "    async function quickchart(key) {\n",
                            "      const quickchartButtonEl =\n",
                            "        document.querySelector('#' + key + ' button');\n",
                            "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
                            "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
                            "      try {\n",
                            "        const charts = await google.colab.kernel.invokeFunction(\n",
                            "            'suggestCharts', [key], {});\n",
                            "      } catch (error) {\n",
                            "        console.error('Error during call to suggestCharts:', error);\n",
                            "      }\n",
                            "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
                            "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
                            "    }\n",
                            "    (() => {\n",
                            "      let quickchartButtonEl =\n",
                            "        document.querySelector('#df-c5376dec-77a9-4769-92d4-32d9bf6f36fb button');\n",
                            "      quickchartButtonEl.style.display =\n",
                            "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
                            "    })();\n",
                            "  </script>\n",
                            "</div>\n",
                            "    </div>\n",
                            "  </div>\n"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 46
                }
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "vYNxOwElckgr",
                "outputId": "8df64b30-1ec1-43b4-a2de-186c500422fd",
                "colab": {
                    "base_uri": "https://localhost:8080/",
                    "height": 677
                },
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1699417553001,
                    "user_tz": 300,
                    "elapsed": 4214,
                    "user": {
                        "displayName": "王俊博",
                        "userId": "18296041296361088912"
                    }
                }
            },
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "    0                                 track_name   artist_name  pop\n",
                            "0   1                                        猜不透         Della   60\n",
                            "0   2                                       愛不單行      Show Luo   50\n",
                            "0   3                                    走著走著就散了    Ada Zhuang   49\n",
                            "0   4                                       國境之南   Fan Yi Chen   53\n",
                            "0   5                                   親愛的那不是愛情  Angela Chang   58\n",
                            "0   6                                       失落沙洲      LaLa Hsu   59\n",
                            "0   7                                       天外來物     Joker Xue   62\n",
                            "0   8                                        原諒我     Jam Hsiao   49\n",
                            "0   9                                  I Believe   Fan Yi Chen   62\n",
                            "0  10  半句再見 - From \"At Café 6\" / Main Theme Song  Stefanie Sun   53\n",
                            "0  11                                       和平分手  Rachel Liang   51\n",
                            "0  12                                         掉了   A-Mei Chang   59\n",
                            "0  13                                      我爱雨夜花         S.H.E   33\n",
                            "0  14                                     蒲公英的約定      Jay Chou   64\n",
                            "0  15                                      沒那麽簡單           黃小琥   59\n",
                            "0  16                                    不為誰而作的歌        JJ Lin   64\n",
                            "0  17                                       恋人未满         S.H.E   50\n",
                            "0  18                                         模特    Ronghao Li   55\n",
                            "0  19                                      凌晨三點鐘        Z-Chen   46\n",
                            "0  20                                     老爸你别装酷      Tiger Hu    5"
                        ],
                        "text/html": [
                            "\n",
                            "  <div id=\"df-cbab89dd-a2b7-4768-a842-90f036d9c94b\" class=\"colab-df-container\">\n",
                            "    <div>\n",
                            "<style scoped>\n",
                            "    .dataframe tbody tr th:only-of-type {\n",
                            "        vertical-align: middle;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe tbody tr th {\n",
                            "        vertical-align: top;\n",
                            "    }\n",
                            "\n",
                            "    .dataframe thead th {\n",
                            "        text-align: right;\n",
                            "    }\n",
                            "</style>\n",
                            "<table border=\"1\" class=\"dataframe\">\n",
                            "  <thead>\n",
                            "    <tr style=\"text-align: right;\">\n",
                            "      <th></th>\n",
                            "      <th>0</th>\n",
                            "      <th>track_name</th>\n",
                            "      <th>artist_name</th>\n",
                            "      <th>pop</th>\n",
                            "    </tr>\n",
                            "  </thead>\n",
                            "  <tbody>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>1</td>\n",
                            "      <td>猜不透</td>\n",
                            "      <td>Della</td>\n",
                            "      <td>60</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>2</td>\n",
                            "      <td>愛不單行</td>\n",
                            "      <td>Show Luo</td>\n",
                            "      <td>50</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>3</td>\n",
                            "      <td>走著走著就散了</td>\n",
                            "      <td>Ada Zhuang</td>\n",
                            "      <td>49</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>4</td>\n",
                            "      <td>國境之南</td>\n",
                            "      <td>Fan Yi Chen</td>\n",
                            "      <td>53</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>5</td>\n",
                            "      <td>親愛的那不是愛情</td>\n",
                            "      <td>Angela Chang</td>\n",
                            "      <td>58</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>6</td>\n",
                            "      <td>失落沙洲</td>\n",
                            "      <td>LaLa Hsu</td>\n",
                            "      <td>59</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>7</td>\n",
                            "      <td>天外來物</td>\n",
                            "      <td>Joker Xue</td>\n",
                            "      <td>62</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>8</td>\n",
                            "      <td>原諒我</td>\n",
                            "      <td>Jam Hsiao</td>\n",
                            "      <td>49</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>9</td>\n",
                            "      <td>I Believe</td>\n",
                            "      <td>Fan Yi Chen</td>\n",
                            "      <td>62</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>10</td>\n",
                            "      <td>半句再見 - From \"At Café 6\" / Main Theme Song</td>\n",
                            "      <td>Stefanie Sun</td>\n",
                            "      <td>53</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>11</td>\n",
                            "      <td>和平分手</td>\n",
                            "      <td>Rachel Liang</td>\n",
                            "      <td>51</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>12</td>\n",
                            "      <td>掉了</td>\n",
                            "      <td>A-Mei Chang</td>\n",
                            "      <td>59</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>13</td>\n",
                            "      <td>我爱雨夜花</td>\n",
                            "      <td>S.H.E</td>\n",
                            "      <td>33</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>14</td>\n",
                            "      <td>蒲公英的約定</td>\n",
                            "      <td>Jay Chou</td>\n",
                            "      <td>64</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>15</td>\n",
                            "      <td>沒那麽簡單</td>\n",
                            "      <td>黃小琥</td>\n",
                            "      <td>59</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>16</td>\n",
                            "      <td>不為誰而作的歌</td>\n",
                            "      <td>JJ Lin</td>\n",
                            "      <td>64</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>17</td>\n",
                            "      <td>恋人未满</td>\n",
                            "      <td>S.H.E</td>\n",
                            "      <td>50</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>18</td>\n",
                            "      <td>模特</td>\n",
                            "      <td>Ronghao Li</td>\n",
                            "      <td>55</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>19</td>\n",
                            "      <td>凌晨三點鐘</td>\n",
                            "      <td>Z-Chen</td>\n",
                            "      <td>46</td>\n",
                            "    </tr>\n",
                            "    <tr>\n",
                            "      <th>0</th>\n",
                            "      <td>20</td>\n",
                            "      <td>老爸你别装酷</td>\n",
                            "      <td>Tiger Hu</td>\n",
                            "      <td>5</td>\n",
                            "    </tr>\n",
                            "  </tbody>\n",
                            "</table>\n",
                            "</div>\n",
                            "    <div class=\"colab-df-buttons\">\n",
                            "\n",
                            "  <div class=\"colab-df-container\">\n",
                            "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-cbab89dd-a2b7-4768-a842-90f036d9c94b')\"\n",
                            "            title=\"Convert this dataframe to an interactive table.\"\n",
                            "            style=\"display:none;\">\n",
                            "\n",
                            "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
                            "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
                            "  </svg>\n",
                            "    </button>\n",
                            "\n",
                            "  <style>\n",
                            "    .colab-df-container {\n",
                            "      display:flex;\n",
                            "      gap: 12px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert {\n",
                            "      background-color: #E8F0FE;\n",
                            "      border: none;\n",
                            "      border-radius: 50%;\n",
                            "      cursor: pointer;\n",
                            "      display: none;\n",
                            "      fill: #1967D2;\n",
                            "      height: 32px;\n",
                            "      padding: 0 0 0 0;\n",
                            "      width: 32px;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-convert:hover {\n",
                            "      background-color: #E2EBFA;\n",
                            "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
                            "      fill: #174EA6;\n",
                            "    }\n",
                            "\n",
                            "    .colab-df-buttons div {\n",
                            "      margin-bottom: 4px;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert {\n",
                            "      background-color: #3B4455;\n",
                            "      fill: #D2E3FC;\n",
                            "    }\n",
                            "\n",
                            "    [theme=dark] .colab-df-convert:hover {\n",
                            "      background-color: #434B5C;\n",
                            "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
                            "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
                            "      fill: #FFFFFF;\n",
                            "    }\n",
                            "  </style>\n",
                            "\n",
                            "    <script>\n",
                            "      const buttonEl =\n",
                            "        document.querySelector('#df-cbab89dd-a2b7-4768-a842-90f036d9c94b button.colab-df-convert');\n",
                            "      buttonEl.style.display =\n",
                            "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
                            "\n",
                            "      async function convertToInteractive(key) {\n",
                            "        const element = document.querySelector('#df-cbab89dd-a2b7-4768-a842-90f036d9c94b');\n",
                            "        const dataTable =\n",
                            "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
                            "                                                    [key], {});\n",
                            "        if (!dataTable) return;\n",
                            "\n",
                            "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
                            "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
                            "          + ' to learn more about interactive tables.';\n",
                            "        element.innerHTML = '';\n",
                            "        dataTable['output_type'] = 'display_data';\n",
                            "        await google.colab.output.renderOutput(dataTable, element);\n",
                            "        const docLink = document.createElement('div');\n",
                            "        docLink.innerHTML = docLinkHtml;\n",
                            "        element.appendChild(docLink);\n",
                            "      }\n",
                            "    </script>\n",
                            "  </div>\n",
                            "\n",
                            "\n",
                            "<div id=\"df-c6d9dad3-7569-4420-b670-8edac2492c21\">\n",
                            "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c6d9dad3-7569-4420-b670-8edac2492c21')\"\n",
                            "            title=\"Suggest charts\"\n",
                            "            style=\"display:none;\">\n",
                            "\n",
                            "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
                            "     width=\"24px\">\n",
                            "    <g>\n",
                            "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
                            "    </g>\n",
                            "</svg>\n",
                            "  </button>\n",
                            "\n",
                            "<style>\n",
                            "  .colab-df-quickchart {\n",
                            "      --bg-color: #E8F0FE;\n",
                            "      --fill-color: #1967D2;\n",
                            "      --hover-bg-color: #E2EBFA;\n",
                            "      --hover-fill-color: #174EA6;\n",
                            "      --disabled-fill-color: #AAA;\n",
                            "      --disabled-bg-color: #DDD;\n",
                            "  }\n",
                            "\n",
                            "  [theme=dark] .colab-df-quickchart {\n",
                            "      --bg-color: #3B4455;\n",
                            "      --fill-color: #D2E3FC;\n",
                            "      --hover-bg-color: #434B5C;\n",
                            "      --hover-fill-color: #FFFFFF;\n",
                            "      --disabled-bg-color: #3B4455;\n",
                            "      --disabled-fill-color: #666;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart {\n",
                            "    background-color: var(--bg-color);\n",
                            "    border: none;\n",
                            "    border-radius: 50%;\n",
                            "    cursor: pointer;\n",
                            "    display: none;\n",
                            "    fill: var(--fill-color);\n",
                            "    height: 32px;\n",
                            "    padding: 0;\n",
                            "    width: 32px;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart:hover {\n",
                            "    background-color: var(--hover-bg-color);\n",
                            "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
                            "    fill: var(--button-hover-fill-color);\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-quickchart-complete:disabled,\n",
                            "  .colab-df-quickchart-complete:disabled:hover {\n",
                            "    background-color: var(--disabled-bg-color);\n",
                            "    fill: var(--disabled-fill-color);\n",
                            "    box-shadow: none;\n",
                            "  }\n",
                            "\n",
                            "  .colab-df-spinner {\n",
                            "    border: 2px solid var(--fill-color);\n",
                            "    border-color: transparent;\n",
                            "    border-bottom-color: var(--fill-color);\n",
                            "    animation:\n",
                            "      spin 1s steps(1) infinite;\n",
                            "  }\n",
                            "\n",
                            "  @keyframes spin {\n",
                            "    0% {\n",
                            "      border-color: transparent;\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "      border-left-color: var(--fill-color);\n",
                            "    }\n",
                            "    20% {\n",
                            "      border-color: transparent;\n",
                            "      border-left-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "    }\n",
                            "    30% {\n",
                            "      border-color: transparent;\n",
                            "      border-left-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "      border-right-color: var(--fill-color);\n",
                            "    }\n",
                            "    40% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "      border-top-color: var(--fill-color);\n",
                            "    }\n",
                            "    60% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "    }\n",
                            "    80% {\n",
                            "      border-color: transparent;\n",
                            "      border-right-color: var(--fill-color);\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "    }\n",
                            "    90% {\n",
                            "      border-color: transparent;\n",
                            "      border-bottom-color: var(--fill-color);\n",
                            "    }\n",
                            "  }\n",
                            "</style>\n",
                            "\n",
                            "  <script>\n",
                            "    async function quickchart(key) {\n",
                            "      const quickchartButtonEl =\n",
                            "        document.querySelector('#' + key + ' button');\n",
                            "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
                            "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
                            "      try {\n",
                            "        const charts = await google.colab.kernel.invokeFunction(\n",
                            "            'suggestCharts', [key], {});\n",
                            "      } catch (error) {\n",
                            "        console.error('Error during call to suggestCharts:', error);\n",
                            "      }\n",
                            "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
                            "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
                            "    }\n",
                            "    (() => {\n",
                            "      let quickchartButtonEl =\n",
                            "        document.querySelector('#df-c6d9dad3-7569-4420-b670-8edac2492c21 button');\n",
                            "      quickchartButtonEl.style.display =\n",
                            "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
                            "    })();\n",
                            "  </script>\n",
                            "</div>\n",
                            "    </div>\n",
                            "  </div>\n"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 47
                }
            ],
            "source": [
                "Spotifyresult=pd.DataFrame()\n",
                "for i in range(len(test)-1):\n",
                "    if len(Spotifyresult)>=20:\n",
                "        break\n",
                "    ff=sp.recommendations(seed_tracks=list(test.track_uri[1+i:5+i]),limit=2)\n",
                "    for z in range(2):\n",
                "        result=pd.DataFrame([z+(2*i)+1])\n",
                "        result['track_name']=ff['tracks'][z]['name']\n",
                "        result['artist_name']=ff['tracks'][z]['artists'][0]['name']\n",
                "        result['pop'] = ff['tracks'][z][\"popularity\"]\n",
                "        #result['uri']=ff['tracks'][z]['id']\n",
                "        #result['url']=ff['tracks'][z]['external_urls']['spotify']\n",
                "        #result['image']=ff['tracks'][z]['album']['images'][1]['url']\n",
                "        Spotifyresult=pd.concat([Spotifyresult,result],axis=0)\n",
                "Spotifyresult"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "THRl3UHBckgr"
            },
            "outputs": [],
            "source": [
                "#df['sim']=cosine_similarity(df.iloc[:,3:16],playvec.iloc[:,3:16])  #auido features cosine similaritiy\n",
                "#df['sim2']=cosine_similarity(df.loc[:, df.columns.str.startswith('T')|df.columns.str.startswith('A')],playvec.loc[:, playvec.columns.str.startswith('T')|playvec.columns.str.startswith('A')])   #artist & track popularity cosine similaritiy\n",
                "#df['sim3']=cosine_similarity(df.loc[:, df.columns.str.startswith('genre')],playvec.loc[:, playvec.columns.str.startswith('genre')])      #genre cosine similaritiy\n",
                "\n",
                "##equally consider\n",
                "#df['sim4']=(df['sim']+df['sim2']+df['sim3'])/3\n",
                "#df = df.sort_values(['sim4'],ascending = False,kind='stable')\n",
                "\n",
                "##get the list of track uris, we are output 20 tracks\n",
                "#qq=df.groupby('artist_uri').head(5).track_uri.head(20)\n",
                "#aa=sp.tracks(qq[0:20])\n",
                "#Fresult=pd.DataFrame()\n",
                "#for i in range(20):\n",
                "#    result=pd.DataFrame([i])\n",
                "#    result['track_name']=aa['tracks'][i]['name']\n",
                "#    result['artist_name']=aa['tracks'][i]['artists'][0]['name']\n",
                "#    #result['url']=aa['tracks'][i]['external_urls']['spotify']\n",
                "#    result['pop'] = aa['tracks'][i][\"popularity\"]\n",
                "#    #result['image']=aa['tracks'][i]['album']['images'][1]['url']\n",
                "#    Fresult=pd.concat([Fresult,result],axis=0)\n",
                "#Fresult"
            ]
        },
        {
            "cell_type": "code",
            "source": [
                "#df['sim']=cosine_similarity(df.drop(['track_uri', 'artist_uri', 'album_uri'], axis = 1),playvec.drop(['track_uri', 'artist_uri', 'album_uri'], axis = 1)) #find cosine similarity between dataset and playlist in general\n",
                "#df['sim2']=cosine_similarity(df.iloc[:,16:-1],playvec.iloc[:,16:])  #find cosine similarity between dataset and playlist in terms of track & artist genres\n",
                "#df['sim3']=cosine_similarity(df.iloc[:,19:-2],playvec.iloc[:,19:])  #find cosine similarity between dataset and playlist in terms of genres\n",
                "\n",
                "##based on similarity score, high correlated genres will be pioritzed, then artist & track popularity, last the audio features\n",
                "#df = df.sort_values(['sim3','sim2','sim'],ascending = False,kind='stable')\n",
                "\n",
                "##get the list of track uris, we are output 20 tracks\n",
                "#qq=df.groupby('artist_uri').head(5).track_uri.head(20)     #to limit recmmendation by same artist\n",
                "\n",
                "##get recommendation track detail\n",
                "#aa=sp.tracks(qq[0:20])\n",
                "#Fresult=pd.DataFrame()\n",
                "#for i in range(20):\n",
                "#    result=pd.DataFrame([i])\n",
                "#    result['track_name']=aa['tracks'][i]['name']\n",
                "#    result['artist_name']=aa['tracks'][i]['artists'][0]['name']\n",
                "#    #result['url']=aa['tracks'][i]['external_urls']['spotify']\n",
                "#    result['pop'] = aa['tracks'][i][\"popularity\"]\n",
                "#    #result['image']=aa['tracks'][i]['album']['images'][1]['url']\n",
                "#    Fresult=pd.concat([Fresult,result],axis=0)\n",
                "#Fresult"
            ],
            "metadata": {
                "id": "aKg9TjPOdI2g"
            },
            "execution_count": null,
            "outputs": []
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.10.11"
        },
        "vscode": {
            "interpreter": {
                "hash": "e246d2215c418239c9316a1ebf2d8abb44dc50b2e5b0e29defd87143398aa387"
            }
        },
        "colab": {
            "provenance": []
        }
    },
    "nbformat": 4,
    "nbformat_minor": 0
}