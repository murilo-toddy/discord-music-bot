from logging import exception
import discord, sys, os
import youtube_dl, asyncio

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
    


async def play(client, ctx, queue, *url):

    connected = ctx.guild.voice_client
    if not connected:
        await join(ctx)


    if len(url) == 0:
        ctx.channel.send("forneca uma chave p busca")
        return

    link = url[0]
    if link.find("spotify",11,21) != -1:
        #PLAY SPOTIFY
        print("SPOTIFY")
    elif link.find("youtube",11,21) != -1:
        #PLAY youtube
        await youtube_play(client,ctx,queue,*url)
    else:
        urlPesquisa=""
        for i in url:
            urlPesquisa += (i+" ")
        await ctx.channel.send(":musical_note: **Searching** :mag_right: `"+urlPesquisa+"`")
        Dados_Video = youtube_search.YoutubeSearch(urlPesquisa)
        await youtube_play(client,ctx,queue,(Dados_Video["url"]))



async def youtube_play(client, ctx, queue, *url):
    

    if len(url) == 0:
        await ctx.channel.send("precisa passar um url ne arrombado")
        return

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

    if(len(queue)) <=0:
        return

    guild = ctx.guild
    song = os.path.isfile("song.mp3")

    bot_voice = guild.voice_client

    if not bot_voice:
        await join(ctx)

    try:
        if song:
            os.remove("song.mp3")

    except PermissionError:
        await ctx.channel.send("tem musica tocando rei")
        return

    ydl_opt = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

 
    url_entrada = queue[0]      
    
    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
        ydl.download([url_entrada])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            song_name = file
            os.rename(file, "song.mp3")

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio("song.mp3")

    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
   

    # FORCESKIP
    while voice_client.is_playing():
        await asyncio.sleep(1)
        while voice_client.is_paused():
            await asyncio.sleep(1)
    
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)


    ##################################
    #Remove da queue

    if not loop:
        if not loop_queue:
            if len(queue)>0:
                queue.remove(0)
            
        else:
            if len(queue)>0:
                next_song = queue[0]
                queue.remove(0)
                queue.append(next_song)
    #################################

    if voice_client and not voice_client.is_paused() and len(queue)>0:
        #baixar proxima musica da lsita
        await play_next(client, ctx, queue)
    


