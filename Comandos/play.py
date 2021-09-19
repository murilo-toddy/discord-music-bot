import discord, sys
import youtube_dl
import os
import asyncio
import collections

sys.path.append("..")
from EstruturaV2 import Lista


song_name = ""
current_song_url = ""
loop = False
loop_queue = False



async def ChangeLoop():
    global loop
    loop = not loop

async def ChangeLoopQueue():
    global loop_queue
    loop_queue = not loop_queue
    print("Loop queue em estado " + str(loop_queue))

async def ForceSkip():
    global current_song_url
    current_song_url.clear()


async def play(client, ctx, queue, *url):
    
    print('\n [*] \'!play\' command called.')

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
        

async def play_next(client, ctx, queue : Lista):

    global current_song_url 
    global loop
    global loop_queue

    guild = ctx.guild
    song = os.path.isfile("song.mp3")

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

    current_song_url = queue[0]

    if loop:
        url_entrada = current_song_url

    else:
         url_entrada = queue[0]    
    
    current_song_url = url_entrada
        

    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
        ydl.download([url_entrada])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            song_name = file
            os.rename(file, "song.mp3")


    ##################################
    #Remove da queue
    if not loop_queue and len(queue) != 0:
        queue.remove(0)
        
    elif len(queue) != 0 and not loop:
        next_song = queue[0]
        queue.remove(0)
        queue.append(next_song)
    #################################

    bot_voice = guild.voice_client

    if not bot_voice:
        await ctx.author.voice.channel.connect()

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio("song.mp3")

    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
        await ctx.channel.send("vo toca essa musica chamada " + str(song_name[0:len(song_name)-16]))

    
    while voice_client.is_playing():
        await asyncio.sleep(1)
    
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    if voice_client and not voice_client.is_paused() :
        #baixar proxima musica da lsita
        await ctx.channel.send("terminei a musica, vo começa a proxima")
        if not len(queue) == 0:
            await play_next(client, ctx, queue)


