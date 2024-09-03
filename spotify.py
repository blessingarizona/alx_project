import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id='2e911d83a37248e68ac6458470a093e6',
            client_secret='2648d06ddc464bdcbff11f1e4269913d',
            redirect_uri='https://spotify.com/',
            scope='user-library-read'
        ))

    def get_user_liked_songs(self):
        results = self.sp.current_user_saved_tracks(limit=50)
        song_ids = [item['track']['id'] for item in results['items']]
        return song_ids

    def get_recommendations(self, seed_tracks):
        recommendations = self.sp.recommendations(seed_tracks=seed_tracks, limit=10)
        return [{
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album_cover': track['album']['images'][0]['url']
        } for track in recommendations['tracks']]
