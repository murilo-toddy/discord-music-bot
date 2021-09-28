import googleapiclient.discovery, utils

async def BuscaPorPesquisaYoutube(url):

    API_KEY = utils.get_youtube_key()

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    search_response = youtube.search().list(
        q = url,
        part = "id",
        type = "video",
        maxResults = 1,
        regionCode = "BR"
    ).execute()

    videoId = search_response["items"][0]["id"]["videoId"]
    UrlFinal = "https://www.youtube.com/watch?v=" + videoId
    
    return UrlFinal

