import discord, sys
import youtube_dl
import os
import asyncio

sys.path.append("..")
from EstruturaV2 import Lista

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

    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
        ydl.download([queue[0]])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            song_name = file
            os.rename(file, "song.mp3")

    ##################################
    #Remove da queue
    queue.remove(0)
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