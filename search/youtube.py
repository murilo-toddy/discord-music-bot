from re import search
import googleapiclient.discovery, config
from urllib.parse import parse_qs, urlparse
from .search_utils import *

# Extract video or playlist info from URL
async def youtube_play(search_youtube, ctx, queue):
    
    API_KEY = config.get_youtube_key()
    query = parse_qs(urlparse(search_youtube).query, keep_blank_values=True)
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    # Playlist
    try:
        playlist_id = query["list"][0]
        await youtube_playlist(playlist_id, youtube, ctx, queue)
    
    # Single video
    except:    
        await youtube_video(search_youtube, youtube, ctx, queue)



async def youtube_video(search_youtube,youtube,ctx,queue):
    
    IdMusic = search_youtube.split("watch?v=")[1][0:11]
    response = youtube.videos().list(
        part='contentDetails,snippet',
        id = IdMusic,
        regionCode = "BR",
    ).execute()

    SetVideoInfo(ctx,response,queue)
    await ShowMessageVideo( response["items"][0]["snippet"]["title"],ctx,queue)
    return


async def youtube_playlist(playlist_id, youtube, ctx, queue):
    
    request = youtube.playlistItems().list(
        part = "contentDetails",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()

    musics = 0
    playlist_name = ""

    while request is not None:
        response = request.execute()

        for i in range (len(response["items"])):       
            responsePlaylist = youtube.videos().list(
        	part= 'contentDetails,snippet',
        	id = response["items"][i]["contentDetails"]["videoId"]
            ).execute()
            if SetVideoInfo(ctx, responsePlaylist, queue):
                musics += 1

        request = youtube.playlistItems().list_next(request, response)

    await ShowMessagePlaylist(musics, playlist_name, ctx)