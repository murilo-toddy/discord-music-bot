import asyncio, discord
from config import *
from utils import embedded_message
from .search_utils import *
import googleapiclient.discovery

async def spotify_play(url, client, ctx, queue):

    API_KEY = get_youtube_key()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    # Playlist
    if url.find("playlist", 25, 35) != -1:
        playlist_items = spotify.playlist_tracks(url, offset=0, fields="items.track.name,items.track.artists.name", 
                                                    additional_types=["track"])

        await embedded_message(ctx, "Adding Playlist to Queue", "May take a while")

        for i in range(len(playlist_items["items"])):

            if not discord.utils.get(client.voice_clients, guild=ctx.guild): return
            track = playlist_items["items"][i]["track"]
            name = track["name"]
            artist = track["artists"][0]["name"]
            search_spotify = str(name) + " - " + str(artist)
            await spotify_to_queue(search_spotify,youtube,ctx,queue)
        
        await ShowMessagePlaylist(len(playlist_items["items"]), "", ctx)


    # Track
    elif url.find("track", 25, 35) != -1:
        music_info = spotify.track(url)
        search_spotify = music_info["name"] + " - " + music_info["album"]["artists"][0]["name"]
        title = await spotify_to_queue(search_spotify,youtube,ctx,queue)
        await ShowMessageVideo(title, ctx, queue)

    else:
        await ctx.channel.send("Forneça um link para uma Musica / Playist válida")

async def spotify_to_queue(search_spotify,youtube,ctx,queue):

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
        print(" [!!] Error in \'query\'\n      * Could not get video info")
        await embedded_message(ctx, "Not Found", "No results found for your query")
        return

    response = youtube.videos().list(
        part= 'contentDetails,snippet',
        id = video_id,
        regionCode = "BR",
    ).execute()

    SetVideoInfo(ctx, response, queue)
    await asyncio.sleep(0.1)

    return response["items"][0]["snippet"]["title"],
