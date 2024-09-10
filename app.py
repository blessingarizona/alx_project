from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from spotify_client import SpotifyClient
import os

app = Flask(__name__)

# Secret key for session management
app.secret_key = os.urandom(24)

# Initialize SpotifyClient
spotify_client = SpotifyClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Redirect to Spotify's authorization page
    auth_url = spotify_client.get_auth_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        # Exchange the authorization code for an access token and save in session
        token_info = spotify_client.get_access_token(code)
        session['token_info'] = token_info
    return redirect(url_for('index'))

@app.route('/recommendations', methods=['GET'])
def recommendations():
    token_info = session.get('token_info')
    if not token_info:
        return redirect(url_for('login'))

    # Ensure the token is fresh
    token_info = spotify_client.ensure_token(token_info)
    session['token_info'] = token_info

    # Get user's liked songs and generate recommendations
    liked_songs = spotify_client.get_user_liked_songs(token_info)
    if not liked_songs:
        return jsonify({"error": "No liked songs found"})

    recommendations = spotify_client.get_recommendations(liked_songs, token_info)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
