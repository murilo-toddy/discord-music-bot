import asyncio, discord, googleapiclient.discovery
from config import *
from .search_utils import *
from utils import embedded_message
from commands.log import log_error

async def spotify_play(url, client, ctx, queue):

    # Playlist
    if url.find("playlist", 25, 35) != -1:
        playlist_items = spotify.playlist_tracks(url, offset=0, fields="items.track.name,items.track.artists.name",
                                                    additional_types=["track"])

        await embedded_message(ctx, "Adding Playlist to Queue", "May take a while")

        for index in range(len(playlist_items["items"])):
            if not discord.utils.get(client.voice_clients, guild=ctx.guild): return
            track = playlist_items["items"][index]["track"]
            name = track["name"]
            artist = track["artists"][0]["name"]
            search_spotify = str(name) + " - " + str(artist)
            await spotify_to_queue(search_spotify, ctx, queue)
            await asyncio.sleep(0.1)

        await show_message_playlist(len(playlist_items["items"]), "", ctx)

    # Single Track
    elif url.find("track", 25, 35) != -1:
        music_info = spotify.track(url)
        search_spotify = music_info["name"] + " - " + music_info["album"]["artists"][0]["name"]
        title = await spotify_to_queue(search_spotify, ctx, queue)
        await show_message_video(title, ctx, queue)
        await asyncio.sleep(0.1)

    else:
        # TODO mudar para embedded
        await ctx.channel.send("Forneça um link para uma Musica / Playist válida")


async def spotify_to_queue(search_spotify, ctx, queue):

    API_KEY = get_youtube_key()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    search_response = youtube.search().list(
        q = search_spotify,
        part = "id",
        type = "video",
        maxResults = 1,
        regionCode = "BR"
    ).execute()

    try:
        video_id = search_response["items"][0]["id"]["videoId"]

    except:
        log_error("query", "Could not get video info")
        await embedded_message(ctx, "Not Found", "No results found for your query")
        return

    response = youtube.videos().list(
        part= 'contentDetails,snippet',
        id = video_id,
        regionCode = "BR",
    ).execute()

    set_video_info(ctx, response, queue)
    return response["items"][0]["snippet"]["title"]
