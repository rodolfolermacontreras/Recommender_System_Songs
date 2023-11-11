# Recommender_System_Songs
Recommender System for Songs (CMU Advanced ML Class)

# Song Recommender System

This repository contains the implementation of a Song Recommender System using collaborative filtering. The system is designed to provide song recommendations based on user preferences and can handle both existing and new users, as well as new songs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/). This project is built using Python 3.x.

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/song-recommender.git
cd song-recommender
```

Then, set up a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  .venv\Scripts\activate.ps1
  ```
- On Unix or MacOS:
  ```bash
  source venv/bin/activate
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

Your default web browser should open automatically and navigate to the web app, usually hosted at `//localhost:8000/docs`.

## Using the Recommender System

- Find your Spotify playlist ID (e.g., 37i9dQZF1E8NgXcf5gQPXv).
- Use the /recommendations/ endpoint, inputting your Spotify playlist ID.
- Receive a list of recommended tracks based on the analysis.

## Deployment

To deploy this project on a live system, you can use services like Streamlit Sharing, Heroku, or any other cloud platform that supports Python applications.

## Built With

- [Python](https://www.python.org/) - Programming language used
- [FastAPI](https://fastapi.tiangolo.com/) - The framework used to create the API
- [Scikit-learn](https://scikit-learn.org/stable/) - Machine learning library for Python

## Authors

- **Your Name** - *Initial work* - [YourUsername](https://github.com/your-username)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
```
