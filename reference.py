# Main execution function
def main():
    spotify_credentials_file = 'Spotify.yaml'
    spotify_credentials = load_spotify_credentials(spotify_credentials_file)
    sp = local_authenticate_spotify(spotify_credentials)

    # Example playlist ID - replace with the actual ID
    playlist_id = 'spotify:playlist:37i9dQZF1E8NgXcf5gQPXv'

    # Fetch track and artist IDs
    track_ids, artist_ids = get_IDs(sp, playlist_id)

    # Fetch track and artist details
    audio_features, track_details, artist_details = fetch_track_artist_details(
        sp, track_ids, artist_ids)

    data_file_path = './data/1M_processed.csv'
    df = load_and_preprocess_data(data_file_path)

    # Merge data
    df_update, test = preprocess_and_merge_data(
        df, audio_features, track_details, artist_details)

    # Generate playvec by summing the features of the user's playlist
    playvec = pd.DataFrame(test.sum(axis=0)).T

    # Generate recommendations using custom recommender
    custom_recommendations = recommend_tracks(df_update, playvec, sp)

    # Generate recommendations using Spotify's API
    # spotify_recommendations = fetch_spotify_recommendations(test, sp)

    # Print or save the recommended track details
    print("Custom Recommendations:", custom_recommendations)
    # print("Spotify Recommendations:", spotify_recommendations)

    # Save the recommendations to files
    custom_recommendations.to_csv(
        './data/custom_recommendations.csv', index=False)
    # spotify_recommendations.to_csv(
    #    './data/spotify_recommendations.csv', index=False)

    print("Custom recommendations saved to './data/custom_recommendations.csv'")
    # print("Spotify recommendations saved to './data/spotify_recommendations.csv'")


if __name__ == "__main__":
    main()
