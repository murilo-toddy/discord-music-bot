from json import load
from logging import exception
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
from dotenv import load_dotenv
import os
import random
from pyasn1.type.univ import Null

API_KEYS_NUMBER = 10

def GetKey():
    load_dotenv()
    global API_KEYS_NUMBER
    Key = random.randint(1, API_KEYS_NUMBER)
   
    Dic = []
    for i in range(API_KEYS_NUMBER):
        text = "API_KEY"+str(i+1)
        text = os.getenv(text)
        Dic.append(text)
    try:
        Key = Dic[Key]
    except:
        Key = os.getenv('API_KEY1')
    return Key




#extract playlist id from url
def YoutubeGetVideosInfo(url_busca, ctx,queue):
    
    part_string = 'contentDetails,statistics,snippet'

    load_dotenv()
    API_KEY = GetKey()
    print(API_KEY)

    url = url_busca
    query = parse_qs(urlparse(url).query, keep_blank_values=True)

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    try:
        playlist_id = query["list"][0]
    except:
    #Video comum    
        IdMusic = url.split("watch?v=")[1][0:11]
        response = youtube.videos().list(
        	part=part_string,
        	id = IdMusic
        ).execute()

        YoutubeSetVideoInfo(ctx,response,queue)

        return
   

    request = youtube.playlistItems().list(
    part = "contentDetails",
    playlistId = playlist_id,
    maxResults = 50
    )
    response = request.execute()

    playlist_items = []

    while request is not None:
        response = request.execute()

        for i in range (len(response["items"])):       
            responsePlaylist = youtube.videos().list(
        	part=part_string,
        	id = response["items"][i]["contentDetails"]["videoId"]
            ).execute()
            YoutubeSetVideoInfo(ctx,responsePlaylist,queue)
        request = youtube.playlistItems().list_next(request, response)
           
def YoutubeSetVideoInfo(ctx, response,queue):

    Info_Musica = {}

    Hours = ""
    Minutes = ""
    Seconds = ""
    try:
        Duration = response["items"][0]["contentDetails"]["duration"][2:]
    except:
        print("\n\nVideo Indisponivel\n\n")
        return False

    if Duration.find("H") != -1:
        [Hours,Duration] = Duration.split("H")
    if Duration.find("M") != -1:
        [Minutes,Duration] = Duration.split("M")
    if Duration.find("S") != -1:
        [Seconds,Duration] = Duration.split("S")

    Duration = ""

    if Hours != "":
        Duration+= Hours + ":"
    if Minutes != "":
        if len(Minutes) == 1:
            Duration+="0"
        Duration+= Minutes + ":"
    else:
            Duration+= "00:"
    if Seconds == "":
            Duration+= "00"
    else:
        if len(Seconds) == 1:
            Duration+="0"
        Duration+= Seconds

    Info_Musica["title"]= response["items"][0]["snippet"]["title"]
    Info_Musica["id"] = response["items"][0]["id"]
    Info_Musica["url"]= "https://www.youtube.com/watch?v="  + Info_Musica["id"]
    Info_Musica["thumb"]= response["items"][0]["snippet"]["thumbnails"]["high"]["url"]
    Info_Musica["user"]= ctx.message.author.name
    Info_Musica["userAvatar"]= ctx.message.author.avatar_url
    Info_Musica["duration"]= Duration
    Info_Musica["likes"] = response["items"][0]["statistics"]["likeCount"]
    Info_Musica["views"] = response["items"][0]["statistics"]["viewCount"]
    Info_Musica["dislikes"] = response["items"][0]["statistics"]["dislikeCount"]

    print(Info_Musica)

    queue.append(Info_Musica)

    return True
