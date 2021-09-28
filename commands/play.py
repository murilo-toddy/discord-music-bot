import discord, sys, asyncio
from youtube_dl.YoutubeDL import YoutubeDL

sys.path.append("..")
from google_search import YoutubeGetVideosInfo
from data_structure import Queue

import youtube_search
from .join import join

loop = False
loop_queue = False
url_entrada = ""
force_skip = False

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True', 'quiet': True}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

async def change_loop():
    global loop
    loop = not loop
    return loop


async def change_loop_queue():
    global loop_queue
    loop_queue = not loop_queue
    return loop_queue


async def play(client, ctx, queue: Queue, *url):
    connected = ctx.guild.voice_client
    if not connected:
        await join(ctx)

    if len(url) == 0:
        await ctx.channel.send("Você precisa fornecer uma chave de busca ou um URL do Youtube")
        return

    link = url[0]
    if link.find("spotify",11,21) != -1: # Spotify URL
        await ctx.channel.send("Ainda não aceito URLs do Spotify")
        return

    elif link.find("youtube",11,21) != -1: # Youtube URL
        await YoutubeGetVideosInfo(url[0], ctx, queue)
        await youtube_play(client, ctx, queue)
        return
    else: # Search query
        urlPesquisa=""
        for i in url:
            urlPesquisa += (i+" ")
        urlPesquisa = urlPesquisa[:-1] 

        await ctx.channel.send(":musical_note: **Searching** :mag_right: `"+urlPesquisa+"`")
        Info_Music = youtube_search.YoutubeSearch(urlPesquisa)
        await YoutubeGetVideosInfo(Info_Music["url"], ctx, queue)
        await youtube_play(client, ctx, queue)
        return



async def youtube_play(client, ctx, queue: Queue):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    
    if voice_client and voice_client.is_playing():
        return
    else:
        await play_next(client, ctx, queue)
    


async def play_next(client, ctx, queue: Queue):

    global loop
    global loop_queue
    global url_entrada

    if(len(queue)) <= 0:
        return

    guild = ctx.guild

    bot_voice = guild.voice_client

    if not bot_voice:
        await join(ctx)

    url_entrada = queue[0]["url"]
    
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % url_entrada, download=False)['entries'][0]
        except:
            return False

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    if not voice_client.is_playing():
        # try:
        print(" [!] Trying FFMPEG")
        voice_client.play(discord.FFmpegPCMAudio(info['formats'][0]['url'], **FFMPEG_OPTIONS), after=None)
        # except:
        #     print(" [!] Error in playing song")
        #     queue.remove(0)
        #     await play_next(client, ctx, queue)
        #     return

    while voice_client.is_playing():
        await asyncio.sleep(1)
        while voice_client.is_paused():
            await asyncio.sleep(1)

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    ##################################
    # Removes music from queue
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
        await play_next(client, ctx, queue)
    