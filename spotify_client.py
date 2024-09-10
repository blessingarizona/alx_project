import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

class SpotifyClient:
    def __init__(self):
        self.sp_oauth = SpotifyOAuth(
            client_id='2e911d83a37248e68ac6458470a093e6',  # Replace with your Spotify Client ID
            client_secret='2648d06ddc464bdcbff11f1e4269913d',  # Replace with your Spotify Client Secret
            redirect_uri='http://localhost:3000/callback',
            scope='user-library-read'
        )
        self.sp = spotipy.Spotify(auth_manager=self.sp_oauth)

    def get_auth_url(self):
        return self.sp_oauth.get_authorize_url()

    def get_access_token(self, code):
        token_info = self.sp_oauth.get_access_token(code)
        return token_info

    def ensure_token(self, token_info):
        if self.sp_oauth.is_token_expired(token_info):
            token_info = self.sp_oauth.refresh_access_token(token_info['refresh_token'])
        return token_info

    def get_user_liked_songs(self, token_info):
        self.sp = spotipy.Spotify(auth=token_info['access_token'])
        results = self.sp.current_user_saved_tracks(limit=50)
        return [item['track']['id'] for item in results['items']]

    def get_recommendations(self, seed_tracks, token_info):
        self.sp = spotipy.Spotify(auth=token_info['access_token'])
        recommendations = self.sp.recommendations(seed_tracks=seed_tracks[:5], limit=10)
        return [
            {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album_cover': track['album']['images'][0]['url']
            }
            for track in recommendations['tracks']
        ]
