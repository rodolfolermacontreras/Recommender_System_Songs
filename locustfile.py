import random
from locust import HttpUser, constant_pacing, task


class RecommenderSystemUser(HttpUser):
    host = "http://localhost:8000"  # Change this to your FastAPI app's address
    # Simulates a user making a request every second
    wait_time = constant_pacing(1)

    @task
    def get_recommendations(self):
        playlist_id = "37i9dQZF1E8NgXcf5gQPXv"  # Example playlist ID
        self.client.post("/recommendations/",
                         json={"playlist_id": playlist_id})
