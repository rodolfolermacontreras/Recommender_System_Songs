import streamlit as st
import requests

# Function to get recommendations from the FastAPI backend
def get_recommendations(playlist_id):
    response = requests.post("http://localhost:8000/recommendations/", json={"playlist_id": playlist_id})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch recommendations"}

# Function to get Spotify recommendations from the FastAPI backend
def get_spotify_recommendations(playlist_id):
    response = requests.post("http://localhost:8000/recommendations/", json={"playlist_id": playlist_id})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch Spotify recommendations"}

# Streamlit UI layout
def run_streamlit_ui():
    st.title('CMU Music Recommendation System')

    # Input for Spotify Playlist URI
    playlist_uri = st.text_input('Spotify Playlist URI')

    # Create two columns for CMU recommendations and Spotify recommendations
    col1, col2 = st.columns(2)

    if st.button('Get Recommendation'):
        if playlist_uri:
            # CMU recommendations
            with col1:
                st.subheader('CMU Recommendations')
                recommendations = get_recommendations(playlist_uri)
                if "error" not in recommendations:
                    for rec in recommendations["recommendations"]:
                        st.text(f"{rec['track_name']} by {rec['artist_name']}")
                    if st.button('Like', key='like_cmu'):
                        st.write('You liked CMU recommendation!')
                    if st.button('Dislike', key='dislike_cmu'):
                        st.write('You disliked CMU recommendation!')
                else:
                    st.error(recommendations["error"])

            # Spotify recommendations
            with col2:
                st.subheader('Spotify Recommendations')
                spotify_recs = get_spotify_recommendations(playlist_uri)
                if "error" not in spotify_recs:
                    for rec in spotify_recs["recommendations"]:
                        st.text(f"{rec['track_name']} by {rec['artist_name']}")
                    if st.button('Like', key='like_spotify'):
                        st.write('You liked Spotify recommendation!')
                    if st.button('Dislike', key='dislike_spotify'):
                        st.write('You disliked Spotify recommendation!')
                else:
                    st.error(spotify_recs["error"])

if __name__ == "__main__":
    run_streamlit_ui()