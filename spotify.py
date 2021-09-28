import google_search
from Pesquisa import BuscaPorPesquisaYoutube
from utils import *


async def get_spotify_info(url, ctx, queue):

    # Playlist
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

    # Track
    elif url.find("track", 25, 35) != -1:
        music_info = spotify.track(url)
        info = await BuscaPorPesquisaYoutube(music_info["name"] + " - " + music_info["album"]["artists"][0]["name"])
        await google_search.YoutubeGetVideosInfo(info, ctx, queue)

    else:
        await ctx.channel.send("Forneça um link para uma Musica / Playist válida")
