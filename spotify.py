import spotipy, os, youtube_search, google_search
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


async def get_spotify_info(url, ctx, queue):

    load_dotenv()
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_ID"),
        client_secret=os.getenv("SPOTIFY_SECRET")
    ))

    if url.find("playlist", 25, 35) != -1:
        playlist_items = spotify.playlist_tracks(url, offset=0, fields="items.track.name,items.track.artists.name", 
                            additional_types=["track"])

        for i in range(len(playlist_items["items"])):
            track = playlist_items["items"][i]["track"]
            name = track["name"]
            artist = track["artists"][0]["name"]
            query = str(name) + " - " + str(artist)
            info = youtube_search.YoutubeSearch(query)
            await google_search.YoutubeGetVideosInfo(info["url"], ctx, queue)

    else:
        music_info = spotify.track(url)
        info = youtube_search.YoutubeSearch(music_info["name"] + " - " + music_info["album"]["artists"][0]["name"])
        await google_search.YoutubeGetVideosInfo(info["url"], ctx, queue)
