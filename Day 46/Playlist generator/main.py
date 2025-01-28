import requests
import bs4
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


Client_ID = 'YOUR CLIENT ID'
Client_secret = 'YOUR CLIENT SECRET CODE'
Playlist_ID = 'YOUR PLAYLIST ID'
Redirect_url = 'YOUR REDIRECT URL'

response = requests.get('https://www.billboard.com/charts/hot-100/')
soup = bs4.BeautifulSoup(response.text,'html.parser')
titles = soup.find_all(name='li',class_ ='lrv-u-width-100p')

for i in titles:
    name = i.find(name = 'h3')
    if name:
        with open('song_list.txt', 'a', encoding='utf-8') as file:
            name = name.text.strip()
            file.write(f'{name} \n')

jd = Spotify(auth_manager=SpotifyOAuth(
    client_id=Client_ID,
    client_secret=Client_secret,
    redirect_uri= Redirect_url,
    scope="playlist-modify-public"
))

with open('song_list.txt') as file:
    song = file.readlines()
    for i in song:
        results = jd.search(q=i.strip(), type="track", limit=1)
        track = results['tracks']['items'][0]
        id = track['id']
        jd.playlist_add_items(Playlist_ID, [id])
