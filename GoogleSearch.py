import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
from dotenv import load_dotenv
import discord, os, random

API_KEYS_NUMBER = 3
MULTIPLE_KEYS = True

def get_key():
    load_dotenv()

    if MULTIPLE_KEYS:
        global API_KEYS_NUMBER
        key = random.randint(1, API_KEYS_NUMBER)
    
        Dic = []
        for i in range(API_KEYS_NUMBER):
            text = "API_KEY"+str(i+1)
            text = os.getenv(text)
            Dic.append(text)
        try:
            key = Dic[key]
        except:
            key = os.getenv('API_KEY1')

    else:
        key = os.getenv("API_KEY")
    
    return key



# Extract video or playlist info from URL
async def YoutubeGetVideosInfo(url_busca, ctx, queue):
    
    part_string = 'contentDetails,statistics,snippet'

    load_dotenv()
    API_KEY = get_key()

    url = url_busca
    query = parse_qs(urlparse(url).query, keep_blank_values=True)

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    try: # Playlist
        playlist_id = query["list"][0]
    except: # Video comum    
        IdMusic = url.split("watch?v=")[1][0:11]
        response = youtube.videos().list(
        	part=part_string,
        	id = IdMusic
        ).execute()

        YoutubeSetVideoInfo(ctx,response,queue)
        await ShowMessageVideo( response["items"][0]["snippet"]["title"],ctx,queue)
        return
   
    request = youtube.playlistItems().list(
        part = "contentDetails",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()

    
    NumeroMusicas=0
    NomePlaylist = ""

    while request is not None:
        response = request.execute()

        for i in range (len(response["items"])):       
            responsePlaylist = youtube.videos().list(
        	part=part_string,
        	id = response["items"][i]["contentDetails"]["videoId"]
            ).execute()
            if YoutubeSetVideoInfo(ctx,responsePlaylist,queue):
                NumeroMusicas+=1
        request = youtube.playlistItems().list_next(request, response)
    await ShowMessagePlaylist(NumeroMusicas,NomePlaylist,ctx)
           
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

    queue.append(Info_Musica)

    return True

async def ShowMessagePlaylist(NumeroMusicas,NomePlaylist,ctx):


    embedVar = discord.Embed(
        title = '**Playlist Enqueued! '+NomePlaylist+"**",
        description = "Total `"+str(NumeroMusicas)+"` musics were enqueued",
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embedVar)

async def ShowMessageVideo(VideoTittle,ctx,queue):

    if len(queue)==1:
        desc="["+str(VideoTittle)+"]("+str(queue[len(queue)-1]["url"])+") was enqueued\n\nPlaying Now!"
    else:
        desc="["+str(VideoTittle)+"]("+str(queue[len(queue)-1]["url"])+") was enqueued\n\nPosition in queue `"+str(len(queue)-1)+"`"

    embedVar = discord.Embed(
        title = "**Video Enqueued!**",
        description =desc,
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embedVar)

