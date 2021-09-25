from logging import exception
import discord, sys, os
import youtube_dl, asyncio

from youtube_dl.YoutubeDL import YoutubeDL

sys.path.append("..")
from EstruturaV2 import Lista

import youtube_search

from .join import join

current_song_url = ""
loop = False
loop_queue = False
url_entrada = ""
song_name = ""
force_skip = False

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


async def GetCurrentURL():
    return url_entrada

async def GetMusicName():
    return str(song_name[0:len(song_name)-16])

async def ChangeLoop():
    global loop
    loop = not loop
    return loop


async def ChangeLoopQueue():
    global loop_queue
    loop_queue = not loop_queue
    return loop_queue

async def ForceSkip():
    global force_skip
    force_skip = True
    

async def GetYoutubeUrl(URL):

    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
    video = ""

    with ydl:
        result = ydl.extract_info \
        (URL,
        download=False) #We just want to extract the info

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries']
        print("Playlist")

        #loops entries to grab each video_url
        for i, item in enumerate(video):
            video = result['entries'][i]
            print(video['webpage_url'])
    else:
        print("Apenas Link")  
        print(URL)  


async def play(client, ctx, queue, *url):
    connected = ctx.guild.voice_client
    if not connected:
        await join(ctx)

    if len(url) == 0:
        await ctx.channel.send("Você precisa fornecer uma chave de busca / URL")
        return

    link = url[0]
    if link.find("spotify",11,21) != -1:
        #PLAY SPOTIFY
        print("SPOTIFY")
    elif link.find("youtube",11,21) != -1:
        #PLAY youtube
        await youtube_play(client, ctx, queue, *url)
    else:
        
        urlPesquisa=""
        for i in url:
            urlPesquisa += (i+" ")
        urlPesquisa = urlPesquisa[:-1] 

        await ctx.channel.send(":musical_note: **Searching** :mag_right: `"+urlPesquisa+"`")
        Info_Music = youtube_search.YoutubeSearch(urlPesquisa)
        await youtube_play(client, ctx, queue, (Info_Music["url"]))



async def youtube_play(client, ctx, queue, *url):
    
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    
    ############################
    # Adicionar novo link na fila
    queue.append(url[0])
    ############################

    
    if voice_client and voice_client.is_playing():
        await ctx.channel.send("vo adiciona essa parada na fila valeu")
        
    else:
        await play_next(client, ctx, queue)
    


async def play_next(client, ctx, queue: Lista):

    global current_song_url 
    global loop
    global loop_queue
    global force_skip
    global url_entrada
    global song_name

    if(len(queue)) <= 0:
        return

    guild = ctx.guild

    bot_voice = guild.voice_client

    if not bot_voice:
        await join(ctx)

    url_entrada = queue[0]      
    
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % url_entrada, download=False)['entries'][0]
        except:
            return False

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio(info['formats'][0]['url'], **FFMPEG_OPTIONS), after=None)

    while voice_client.is_playing():
        await asyncio.sleep(1)
        while voice_client.is_paused():
            await asyncio.sleep(1)
    
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    ##################################
    #Remove da queue
    if not loop:
        if not loop_queue:
            if len(queue) > 0:
                queue.remove(0)
            
        else:
            if len(queue) > 0:
                next_song = queue[0]
                queue.remove(0)
                queue.append(next_song)
    #################################

    if voice_client and not voice_client.is_paused() and len(queue) > 0:
        #baixar proxima musica da lsita
        await play_next(client, ctx, queue)
    
