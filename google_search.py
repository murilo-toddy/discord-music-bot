import discord, googleapiclient.discovery, config
from urllib.parse import parse_qs, urlparse


# Extract video or playlist info from URL
async def YoutubeGetVideosInfo(url_busca, ctx, queue):
    
    part_string = 'contentDetails,statistics,snippet'

    API_KEY = config.get_youtube_key()

    url = url_busca
    query = parse_qs(urlparse(url).query, keep_blank_values=True)

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

    try: # Playlist
        playlist_id = query["list"][0]
    except: # Video comum    
        IdMusic = url.split("watch?v=")[1][0:11]
        response = youtube.videos().list(
        	part=part_string,
        	id = IdMusic,
            regionCode = "BR",
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

    
    musics = 0
    playlist_name = ""

    while request is not None:
        response = request.execute()

        for i in range (len(response["items"])):       
            responsePlaylist = youtube.videos().list(
        	part=part_string,
        	id = response["items"][i]["contentDetails"]["videoId"]
            ).execute()
            if YoutubeSetVideoInfo(ctx, responsePlaylist, queue):
                musics += 1

        request = youtube.playlistItems().list_next(request, response)

    await ShowMessagePlaylist(musics, playlist_name, ctx)


def YoutubeSetVideoInfo(ctx, response,queue):
    music_info = {}

    hours = ""
    minutes = ""
    seconds = ""
    try:
        duration = response["items"][0]["contentDetails"]["duration"][2:]
    except:
        print("\n\n [!] Video unavailable\n\n")
        return False

    if duration.find("H") != -1:
        [hours,duration] = duration.split("H")
    if duration.find("M") != -1:
        [minutes,duration] = duration.split("M")
    if duration.find("S") != -1:
        [seconds,duration] = duration.split("S")

    duration = ""

    if hours != "":
        duration+= hours + ":"
    if minutes != "":
        if len(minutes) == 1:
            duration+="0"
        duration+= minutes + ":"
    else:
            duration+= "00:"
    if seconds == "":
            duration+= "00"
    else:
        if len(seconds) == 1:
            duration+="0"
        duration+= seconds

    music_info["title"] = response["items"][0]["snippet"]["title"]
    music_info["id"] = response["items"][0]["id"]
    music_info["url"] = "https://www.youtube.com/watch?v=" + music_info["id"]
    music_info["thumb"] = response["items"][0]["snippet"]["thumbnails"]["high"]["url"]
    music_info["duration"] = duration
    # music_info["views"] = response["items"][0]["statistics"]["viewCount"]
    # music_info["likes"] = response["items"][0]["statistics"]["likeCount"]
    # music_info["dislikes"] = response["items"][0]["statistics"]["dislikeCount"]
    music_info["user"] = ctx.message.author.name
    music_info["userAvatar"]= ctx.message.author.avatar_url

    queue.append(music_info)
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
        description = desc,
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embedVar)
