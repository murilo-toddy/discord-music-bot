import spotipy, os, youtube_search, google_search
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from Pesquisa import BuscaPorPesquisaYoutube


async def get_spotify_info(url, ctx, queue):

    if os.path.isfile("./.env"):
        load_dotenv()
        CLIENT_ID = os.getenv("SPOTIFY_ID")
        CLIENT_SECRET = os.getenv("SPOTIFY_SECRET")

    else:
        CLIENT_ID = os.environ['SPOTIFY_ID']
        CLIENT_SECRET = os.environ['SPOTIFY_SECRET']
    
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET
    ))

    if url.find("playlist", 25, 35) != -1:
        playlist_items = spotify.playlist_tracks(url, offset=0, fields="items.track.name,items.track.artists.name", 
                            additional_types=["track"])

        for i in range(len(playlist_items["items"])):
            track = playlist_items["items"][i]["track"]
            name = track["name"]
            artist = track["artists"][0]["name"]
            query = str(name) + " - " + str(artist)
            info = await BuscaPorPesquisaYoutube(query)
            await google_search.YoutubeGetVideosInfo(info, ctx, queue)

    else:
        music_info = spotify.track(url)
        info = await BuscaPorPesquisaYoutube(music_info["name"] + " - " + music_info["album"]["artists"][0]["name"])
        await google_search.YoutubeGetVideosInfo(info, ctx, queue)
