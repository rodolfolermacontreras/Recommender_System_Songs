# CMU Music Recommender System

Welcome to the CMU Music Recommender System, a sophisticated tool for discovering new music. This system uses advanced machine learning techniques to provide personalized song recommendations, based on user preferences and Spotify playlist analysis.

![Logo](demo.PNG)

## About the Algorithm

The system employs collaborative filtering and feature extraction to analyze Spotify playlists, using the Spotify API to fetch audio features and artist details. It then applies algorithms like TF-IDF Vectorization and Cosine Similarity to suggest songs that match the user's musical taste.

## Getting Started

These instructions will help you get the project up and running on your local machine for development, testing, and usage.

If at any point you need more guidance I recommend the following articule for more step by step guidance: [Managing Git Repositories with VSCode](https://medium.com/@dipan.saha/managing-git-repositories-with-vscode-setting-up-a-virtual-environment-62980b9e8106)

### Prerequisites

Ensure you have Python 3.x installed. Download it from [here](https://www.python.org/downloads/).

### Installation

Clone the repository:

```bash
git clone https://github.com/rodolfolermacontreras/Recommender_System_Songs.git
cd music-recommender
```

Then, set up a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  .\.venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```bash
  source .venv/bin/activate
  ```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Web App

To run the Streamlit web app, execute:

```bash
uvicorn main:app --reload
```

Your default web browser should open automatically and navigate to the web app, usually hosted at `http://localhost:8000/docs`.

### Running the Tests

To run the automated tests for this system, use pytest:

```bash
pytest
```

### Performing a Load Test with Locust

To perform a load test on the system, use Locust:

1. Ensure Locust is installed:
```bash
pip install locust
```
2. Run Locust:
```bash
locust
```
3. Access the Locust web interface at `http://localhost:8089` and configure your test parameters.

## Using the Recommender System

- Find your Spotify playlist ID (e.g., 37i9dQZF1E8NgXcf5gQPXv).
- Use the /recommendations/ endpoint, inputting your Spotify playlist ID.
- Receive a list of recommended tracks based on the analysis.

## Deployment

To deploy this project on a live system, you can use services like Streamlit Sharing, Heroku, or any other cloud platform that supports Python applications.

## Repository Structure and Dependencies
  `fetch_track_artist_details.py`: Fetches track and artist details from Spotify.
  `main.py`: The main FastAPI application.
  `preprocess_and_merge_data.py`: Processes and merges data for the recommender system.
  `test_app.py`: Contains pytest tests for the API.
  `requirements.txt`: Lists all the Python dependencies.
  `locustfile.py`: Configuration for Locust load testing.
  `.venv`: Virtual environment for the project.


## Built With

- [Python](https://www.python.org/) - Programming language used
- [FastAPI](https://fastapi.tiangolo.com/) - The framework used to create the API 
- [Scikit-learn](https://scikit-learn.org/stable/) - Machine learning library for Python
- [Spotify Web API](https://developer.spotify.com/documentation/web-api)

## Authors

- **Your Name** - *Initial work* - [YourUsername](https://github.com/your-username)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
```
