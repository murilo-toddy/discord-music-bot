import os, youtube_dl, discord
from main import client
import asyncio

@client.command(aliases=['p'])
async def play(ctx, url : str):
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
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            song_name = file
            os.rename(file, "song.mp3")

    guild = ctx.guild
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
    
    # if voice_client:
        # await ctx.voice_client.disconnect()
