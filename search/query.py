import asyncio
import googleapiclient.discovery, config
from utils import embedded_message
from .search_utils import *

async def query_play(ctx, search_query, queue):

    API_KEY = config.get_youtube_key()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    search_response = youtube.search().list(
        q = search_query,
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

    set_video_info(ctx, response, queue)
    await asyncio.sleep(0.1)
    await show_message_video(response["items"][0]["snippet"]["title"], ctx, queue)
    return
    