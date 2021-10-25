import asyncio, discord
import googleapiclient.discovery, config
from urllib.parse import parse_qs, urlparse
from .search_utils import *
from utils import embedded_message

# Extract video or playlist info from URL
async def youtube_play(search_youtube, client, ctx, queue):
    
    query = parse_qs(urlparse(search_youtube).query, keep_blank_values=True)

    try:
        # Playlist
        playlist_id = query["list"][0]
        await youtube_playlist(playlist_id, client, ctx, queue)
    
    except:
        # Single video
        await youtube_video(search_youtube, ctx, queue)


async def youtube_video(search_youtube,ctx,queue):
    
    API_KEY = config.get_youtube_key()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    music_id = search_youtube.split("watch?v=")[1][0:11]
    response = youtube.videos().list(
        part='contentDetails,snippet',
        id = music_id,
        regionCode = "BR",
    ).execute()

    set_video_info(ctx,response,queue)
    await show_message_video( response["items"][0]["snippet"]["title"], ctx, queue)
    await asyncio.sleep(0.1)
    return


async def youtube_playlist(playlist_id, client, ctx, queue):
    
    API_KEY = config.get_youtube_key()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    request = youtube.playlistItems().list(
        part = "contentDetails",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()

    musics = 0
    playlist_name = ""

    await embedded_message(ctx, "Adding Playlist to Queue", "May take a while")

    while request is not None:
        response = request.execute()

        for i in range (len(response["items"])):
            if not discord.utils.get(client.voice_clients, guild=ctx.guild): return

            responsePlaylist = youtube.videos().list(
        	part= 'contentDetails,snippet',
        	id = response["items"][i]["contentDetails"]["videoId"]
            ).execute()
            
            if set_video_info(ctx, responsePlaylist, queue):
                musics += 1

            if musics == 1 or musics % 5 == 0:
                await asyncio.sleep(0.1)

        request = youtube.playlistItems().list_next(request, response)

    await show_message_playlist(musics, playlist_name, ctx)