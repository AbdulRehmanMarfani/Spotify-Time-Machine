from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import os

spotify_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_url = os.getenv("SPOTIPY_REDIRECT_URI")

date = str(input("Which date do you want to travel to? (YYYY-MM-DD): "))
url = f"https://www.billboard.com/charts/hot-100/{date}/"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0"
}
response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
top100_songs = [song.text for song in soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")]
top100_songs = [song.strip() for song in top100_songs if song.strip()]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri=redirect_url,
    scope="playlist-read-private playlist-read-collaborative playlist-modify-private",
    cache_path=".cache-spotify"
))
song_urls = []
for song in top100_songs:
    results = sp.search(q=song, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        song_urls.append(track['external_urls']['spotify'])
    else:
        song_urls.append(f"Song '{song}' not found on Spotify.")

playlist_name = f"Billboard Hot 100 - {date}"
playlist_description = f"Top 100 songs from Billboard Hot 100 on {date}"

user = sp.current_user()

def get_all_playlists(sp):
    playlists = []
    results = sp.current_user_playlists()
    playlists.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        playlists.extend(results['items'])
    return playlists

all_playlists = get_all_playlists(sp)

playlist_id = None
for playlist in all_playlists:
    if playlist['name'] == playlist_name:
        print(f"Playlist '{playlist_name}' already exists with ID: {playlist['id']}\nURL: {playlist['external_urls']['spotify']}")
        playlist_id = playlist['id']
        break

if not playlist_id:
    user = sp.current_user()
    playlist = sp.user_playlist_create(user['id'], name=playlist_name, public=False, description=playlist_description)
    playlist_id = playlist['id']
    for song in song_urls:
        if "not found" not in song:
            sp.playlist_add_items(playlist_id, [song])
        else:
            print(song)
