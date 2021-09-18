import os
import discord, youtube_dl
from discord.voice_client import VoiceClient
import asyncio
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("\n [*] The bot is running.")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print("\n [*] The bot's status was successfully set.")


# @client.event
# async def on_message(message):
#     if message.author == client.useru:
#         return   

#     if message.content.startswith("!hello"):
#         await message.channel.send("yes")


@client.command()
async def join(ctx):

    print('\n [*] \'!join\' command called.')

    bot_channel = ctx.guild.voice_client
    
    if bot_channel:
        await ctx.channel.send("ja to conectado parsa")
    
    else:
        await ctx.author.voice.channel.connect()
        voice = ctx.guild.voice_client
        voice.pause()



@client.command()
async def leave(ctx):
    
    print('\n [*] \'!leave\' command called.')

    voice = ctx.guild.voice_client

    if voice:
        await ctx.channel.send("To de saidas")
        await ctx.voice_client.disconnect()

    else:
        await ctx.channel.send("Não to conectado")



@client.command(brief="", aliases=["p"])
async def play(ctx, *url):

    print('\n [*] \'!play\' command called.')

    if len(url) == 0:
        await ctx.channel.send("precisa passar um url ne arrombado")
        return

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    
    if voice_client and voice_client.is_playing():
        await ctx.channel.send("vo adiciona essa parada na fila valeu")
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
        await ctx.channel.send("terminei a musica, vo começa a proxima")


@client.command()
async def pause(ctx):

    print('\n [*] \'!pause\' command called.')

    voice_client:  discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await ctx.channel.send("Nao to conectado")
    
    elif not voice_client.is_playing() or voice_client.is_paused():
        await ctx.channel.send("nao to tocando")

    else:
        voice_client.pause()
        await ctx.channel.send("Pausado pattern")



@client.command()
async def resume(ctx):

    print('\n [*] \'!resume\' command called.')

    voice_client:  discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await ctx.channel.send("nao to conectado")

    elif voice_client.is_playing() or not voice_client.is_paused():
        await ctx.channel.send("nao to pausado")
    
    else:
        voice_client.resume()
        await ctx.channel.send("vortei")



if __name__ == '__main__':
    client.run(TOKEN)


