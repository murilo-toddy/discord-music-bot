import googleapiclient.discovery, config

async def BuscaPorPesquisaYoutube(url):

    API_KEY = config.get_youtube_key()

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    search_response = youtube.search().list(
        q = url,
        part = "id",
        type = "video",
        maxResults = 1,
        regionCode = "BR"
    ).execute()

    try:
        video_id = search_response["items"][0]["id"]["videoId"]
        final_url = "https://www.youtube.com/watch?v=" + video_id
        return final_url

    except:
        print(" [!!] Error in \'youtube_search\'\n      * Could not convert to URL")
        return False

