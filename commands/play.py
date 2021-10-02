import discord, asyncio
from youtube_dl.YoutubeDL import YoutubeDL
from google_search import YoutubeGetVideosInfo
from search import BuscaPorPesquisaYoutube
from spotify import get_spotify_info
from .join import join
from utils import *

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True', 'quiet': True,}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


async def play(client, ctx, queue, bot_info, counter, *args):
    connected = ctx.guild.voice_client
    if not connected:
        await join(ctx)

    if len(args) == 0:
        await embedded_message(ctx, "Hey, nerd!", "You need to provide a search key\nlike a query or a music URL")
        return

    url = args[0]
    if url.find("spotify",11,21) != -1: # Spotify URL
        await get_spotify_info(url, ctx, queue)
        await youtube_play(client, ctx, queue, bot_info, counter)
        return

    elif url.find("youtube",11,21) != -1: # Youtube URL
        await YoutubeGetVideosInfo(url, ctx, queue)
        await youtube_play(client, ctx, queue, bot_info, counter)
        return
        
    else: # Search query
        search_query = " ".join(args)

        await ctx.channel.send(":musical_note: **Searching** :mag_right: `" + search_query + "`")
        music_info = await BuscaPorPesquisaYoutube(search_query)
        if music_info == False:
            await embedded_message(ctx, "Not Found", "No results found for your query")
            print(" [!!] Error in \'play\'\n      * No results found for query")
            return 
        await YoutubeGetVideosInfo(music_info, ctx, queue)
        await youtube_play(client, ctx, queue, bot_info, counter)
        return



async def youtube_play(client, ctx, queue, bot_info, counter):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    
    if voice_client and voice_client.is_playing():
        return
    else:
        await play_next(client, ctx, queue, bot_info, counter)



async def play_next(client, ctx, queue, bot_info, counter):

    if(len(queue)) <= 0:
        return

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    if not voice_client:
        await join(ctx)

    music_url = queue[0]["url"]
    
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            print(" [!] Extracting music info")
            info = ydl.extract_info("ytsearch:%s" % music_url, download=False)['entries'][0]
        except:
            return False


    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    if bot_info.get_seek():
        FFMPEG_OPTIONS["before_options"] = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -ss ' + str(bot_info.get_seek_time())
        await counter.set_time(bot_info.get_seek_time())

    if voice_client and not voice_client.is_playing():
        print(" [!] Trying FFMPEG")

        try:
            voice_client.play(discord.FFmpegPCMAudio(info['formats'][0]['url'], **FFMPEG_OPTIONS), after=None)

        except:
            print(" [!!] Error in \'play\' function\n      * Error in FFMPEG conversion")
            await embedded_message(ctx, "**Error in Conversion**", "_Music could not be converted_\n" +
                                                                    "_Sorry for the inconvenience_")

        if bot_info.get_seek():
            FFMPEG_OPTIONS["before_options"] = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
        
        else:
            await counter.reset()


    if bot_info.get_seek():
        bot_info.seek_set_false()

    while voice_client.is_playing():
        await asyncio.sleep(1)
        while voice_client.is_paused():
            await asyncio.sleep(1)

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    ##################################
    # Removes music from queue
    if not bot_info.get_loop() and not bot_info.get_seek():
        if not bot_info.get_loop_queue():
            if len(queue) > 0:
                queue.remove(0)
            
        else:
            if len(queue) > 0:
                next_song = queue[0]
                queue.remove(0)
                queue.append(next_song)

    #################################
    
   

    if voice_client and not voice_client.is_paused() and len(queue) > 0:
        await counter.reset()
        await play_next(client, ctx, queue, bot_info, counter)
    