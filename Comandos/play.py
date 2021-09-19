import discord
import youtube_dl
import os
import asyncio

async def play(client, ctx, *url):
    
    print('\n [*] \'!play\' command called.')

    if len(url) == 0:
        await ctx.channel.send("precisa passar um url ne arrombado")
        return

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    
    if voice_client and voice_client.is_playing():
        await ctx.channel.send("vo adiciona essa parada na fila valeu")
        # Adicionar novo link na fila
        return


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
        ydl.download([url[0]])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            song_name = file
            os.rename(file, "song.mp3")

    bot_voice = guild.voice_client

    if not bot_voice:
        await ctx.author.voice.channel.connect()

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio("song.mp3")

    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
        await ctx.channel.send("vo toca essa musica chamada " + str(song_name[0:len(song_name)-16]))

    else:
        await ctx.channel.send("vo adiciona na lista")

    while voice_client.is_playing():
        await asyncio.sleep(1)
    
    if voice_client:
        #baixar proxima musica da lsita
        await ctx.channel.send("terminei a musica, vo começa a proxima")