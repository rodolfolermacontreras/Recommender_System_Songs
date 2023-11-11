from fastapi.testclient import TestClient
import pytest
from main import app  # Import the FastAPI app from main.py

client = TestClient(app)


@pytest.mark.asyncio
async def test_get_recommendations(mocker):
    # Mocking Spotify interaction and other functions
    mocker.patch('main.fetch_track_artist_details',
                 return_value=([{}], [{}], [{}]))
    mocker.patch('main.recommend_tracks', return_value='Test recommendation')

    # Arrange
    request_body = {"playlist_id": "37i9dQZF1E8NgXcf5gQPXv"}

    # Act
    response = client.post("/recommendations/", json=request_body)

    # Assert
    assert response.status_code == 200
    assert "recommendations" in response.json()
