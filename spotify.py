from google_search import YoutubeGetVideosInfo
from search import BuscaPorPesquisaYoutube
from config import *

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
            await add_to_queue(ctx, queue, query)

    # Track
    elif url.find("track", 25, 35) != -1:
        music_info = spotify.track(url)
        query = music_info["name"] + " - " + music_info["album"]["artists"][0]["name"]
        await add_to_queue(ctx, queue, query)

    else:
        await ctx.channel.send("Forneça um link para uma Musica / Playist válida")


async def add_to_queue(ctx, queue, query):
    info = await BuscaPorPesquisaYoutube(query)
    await YoutubeGetVideosInfo(info, ctx, queue)