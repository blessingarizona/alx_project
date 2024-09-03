from flask import Flask, render_template, jsonify, request
from spotify import SpotifyClient

app = Flask(__name__)
spotify_client = SpotifyClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_liked_songs = spotify_client.get_user_liked_songs()
    recommendations = spotify_client.get_recommendations(user_liked_songs)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
