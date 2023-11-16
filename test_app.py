import pandas as pd
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app  # Import your FastAPI app

client = TestClient(app)


def test_get_recommendations():
    # Arrange
    playlist_id = "37i9dQZF1E8NgXcf5gQPXv"
    # Mock DataFrame for the output of recommend_tracks
    mock_recommendations_df = pd.DataFrame([
        {"track_name": "Test Song", "artist_name": "Test Artist", "pop": 50}
    ])

    with patch('main.fetch_track_artist_details', return_value=(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())), \
            patch('main.load_and_preprocess_data', return_value=pd.DataFrame()), \
            patch('main.preprocess_and_merge_data', return_value=(pd.DataFrame(), pd.DataFrame([0]))), \
            patch('main.recommend_tracks', return_value=mock_recommendations_df):
        # Act
        response = client.post("/recommendations/",
                               json={"playlist_id": playlist_id})

        # Assert
        expected_response = {
            "playlist_id": playlist_id,
            "recommendations": mock_recommendations_df.to_dict(orient='records')
        }
        assert response.status_code == 200
        assert response.json() == expected_response

# Run this test using the pytest command


# Run this test using the pytest command


# from fastapi.testclient import TestClient
# import pandas as pd
# import pytest
# from main import app  # Import the FastAPI app from main.py

# client = TestClient(app)


# @pytest.mark.asyncio
# async def test_get_recommendations(mocker):
#     # Arrange
#     # Mock the Spotify interactions and other dependent functions
#     audio_features_mock = pd.DataFrame({
#         'type': ['dummy_type'],
#         'uri': ['dummy_uri'],
#         'track_href': ['dummy_track_href'],
#         'analysis_url': ['dummy_analysis_url'],
#         'id': ['dummy_id']
#     })

#     # Ensure the track details mock includes the 'Artist_uri' column
#     track_details_mock = pd.DataFrame({
#         'id': ['dummy_id'],
#         'Track_uri': ['dummy_track_uri'],
#         'Artist_uri': ['dummy_artist_uri'],
#         'Album_uri': ['dummy_album_uri'],  # Add this line
#         'other_columns': ['dummy_data']
#     })

#     # Include necessary columns for artist details
#     artist_details_mock = pd.DataFrame({
#         'id': ['dummy_id'],
#         'Artist_uri': ['dummy_artist_uri'],  # Add this line
#         'other_columns': ['dummy_data']  # Include other necessary dummy data
#     })

#     mocker.patch('main.fetch_track_artist_details', return_value=(
#         audio_features_mock, track_details_mock, artist_details_mock))

#     request_body = {"playlist_id": "37i9dQZF1E8NgXcf5gQPXv"}

#     # Act
#     response = client.post("/recommendations/", json=request_body)

#     # Assert
#     assert response.status_code == 200
#     assert "recommendations" in response.json()
