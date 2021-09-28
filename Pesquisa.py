import os, random, googleapiclient.discovery
from dotenv import load_dotenv


API_KEYS_NUMBER = 3
MULTIPLE_KEYS = True


def get_key():
    if MULTIPLE_KEYS:
        global API_KEYS_NUMBER
        dic = []
        key = random.randint(1, API_KEYS_NUMBER)

        if os.path.isfile("./.env"):
            load_dotenv()
        
        for i in range(API_KEYS_NUMBER):
            text = "API_KEY"+str(i+1)
            if os.path.isfile("./.env"): text = os.getenv(text)
            else: text = os.environ[text]
            dic.append(text)
        try:
            key = dic[key]
        except:
            key = os.getenv('API_KEY1')

    else:
        key = os.getenv("API_KEY")
    
    print(key)
    return key

async def BuscaPorPesquisaYoutube(url):

    API_KEY = get_key()

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

