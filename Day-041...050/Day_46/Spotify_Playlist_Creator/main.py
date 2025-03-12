import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()


date_range = input("What year would you like to check? (yyyy-mm-dd)")


SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private user-read-private"
))

# Get the authenticated user’s ID
user_id = sp.current_user()["id"]

# Create a new playlist
playlist = sp.user_playlist_create(user=user_id, name=f'New Top 100 {date_range}', public=False)
playlist_id = playlist['id']
print(f"Playlist created: {playlist['name']} (ID: {playlist['id']})")

URL = f'https://www.billboard.com/charts/billboard-u-s-afrobeats-songs/{date_range}'
URL1 = f'https://www.billboard.com/charts/hot-100/{date_range}'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(URL, headers=header)
website = response.text

soup = BeautifulSoup(website, "html.parser")
song_title = soup.select(".o-chart-results-list__item .c-title")

for title in song_title:
    # Search for a song by name & artist
    song_name = title.getText().strip()
    artist_name = title.next_sibling.next_sibling.getText().strip()
    query = f"track:{song_name} artist:{artist_name}"

    result = sp.search(q=query, limit=1, type="track")

    # Add song to the playlist if found
    if result["tracks"]["items"]:
        song_uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id, [song_uri])
        print(f"Added '{song_name}' by {artist_name} to the playlist!")
    else:
        print("Song not found!")
        pass

