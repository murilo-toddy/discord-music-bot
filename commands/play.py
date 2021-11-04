import discord, asyncio
from youtube_dl.YoutubeDL import YoutubeDL
from search import *
from .join import join
from utils import *
from urllib.error import HTTPError
from youtube_dl.utils import DownloadError

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True', 'quiet': True,'source_address':'0.0.0.0', 'cookiefile': 'cookies.txt'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


async def play(client, ctx, queue, bot_info, counter, *args):

    if not args:
        await embedded_message(ctx, "Hey, nerd!", "You need to provide a search key\nlike a query or a music URL")
        return

    if not ctx.guild.voice_client:
        await join(ctx)
    
    url = args[0]

    loop = asyncio.get_event_loop()
    
    if check_play_next(client, ctx):
        loop.create_task(play_next(client, ctx, queue, bot_info, counter))

    # Spotify URL
    if url.find("spotify",11,21) != -1:
        loop.create_task(search.spotify.spotify_play(url, client, ctx, queue))

    # Youtube URL
    elif url.find("youtube",11,21) != -1:
        loop.create_task(search.youtube.youtube_play(url, client, ctx, queue))

    # Search query
    else:
       loop.create_task(query(args, ctx, queue))



def check_play_next(client, ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    return voice_client and not voice_client.is_playing()


async def play_next(client, ctx, queue, bot_info, counter):

    while not queue: await asyncio.sleep(0.01)

    guild = ctx.guild
    voice_client = discord.utils.get(client.voice_clients, guild=guild)

    if not voice_client:
        await join(ctx)
        voice_client = discord.utils.get(client.voice_clients, guild=guild)

    info = await youtube_extraction(client, ctx, queue, bot_info, counter)

    if info == False: return

    if not await play_song(client, ctx, queue, info, voice_client, bot_info, counter): return
    if not await play_loop(client, ctx, queue, bot_info,counter): return
    if not await check_bot_playing(bot_info, queue): return
    await call_next_song(client, ctx, queue, bot_info, counter)
    


async def youtube_extraction(client, ctx, queue, bot_info, counter):

    if not queue: return False

    music_url = queue[0]["url"]

    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            print(" [!] Extracting music info in "+ ctx.guild.name)
            info = ydl.extract_info("ytsearch:" + str(music_url), download=False)['entries'][0]
            
        except HTTPError as e:
            if  e.code == 429: #Limit of videos exceeded, chama os donos do bot
                print(" [!!] Error in \'play\' function\n      * Ydl limit exceeded")
                await embedded_message(ctx, "**Something broke** :cry:", "Bot will probably be out for a while\n" +
                                                                        "Contact the devs asap!")             
            await call_next_song(client, ctx, queue, bot_info, counter)
            return False

        except DownloadError as e:
            print(" [!!] Error in \'play\' function\n      * {}".format(e))
            await embedded_message(ctx, "**Error in extraction**", "`" + str(queue[0]["title"]) + "`\n" +
                                                                "_was removed from the queue_\n" +
                                                                "_for being age restricted_\n")
            queue.remove(0)
            await call_next_song(client, ctx, queue, bot_info, counter)
            return False
            
        except:
            queue.remove(0)
            print(" [!!] Error in \'play\' function\n      * Unknown error")
            await call_next_song(client, ctx, queue, bot_info, counter)
            await embedded_message(ctx, "**Error in extraction**  :cry:", "Sorry, I am unable to play this song")
            return False

    return info


async def play_song(client,ctx,queue, info, voice_client, bot_info, counter):
    
    if not queue: return False

    if bot_info.get_seek():
        FFMPEG_OPTIONS["before_options"] = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -ss ' + str(bot_info.get_seek_time())
        await counter.set_time(bot_info.get_seek_time())

    if voice_client and not voice_client.is_playing():
        print(" [!] Playing "+str(queue[0]["title"])+" in "+ ctx.guild.name)

        try:
            voice_client.play(discord.FFmpegPCMAudio(info['formats'][0]['url'], **FFMPEG_OPTIONS), after=None)

        except:
            print(" [!!] Error in \'play\' function\n      * Error in FFMPEG conversion")
            await embedded_message(ctx, "**Error in Conversion**", "_Music could not be converted_\n" +
                                                                    "_Sorry for the inconvenience_")
            queue.remove(0)
            await call_next_song(client, ctx, queue, bot_info, counter)
            return False

        if bot_info.get_seek():
            FFMPEG_OPTIONS["before_options"] = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
        
        else:
            await counter.reset()

    if bot_info.get_seek():
        bot_info.seek_set_false()

    return True


async def check_bot_playing(bot_info, queue):

    if not queue: return False

    if not bot_info.get_loop() and not bot_info.get_seek():
        if not bot_info.get_loop_queue():
            if queue:
                queue.remove(0)
        
        elif queue:
            next_song = queue[0]
            queue.remove(0)
            queue.append(next_song)

    return True


async def play_loop(client, ctx, queue,bot_info ,counter):


    print("Entrou loop\n")

    if not queue: return False
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    playing_now_duration = queue[0]["duration_seconds"]

    await counter.reset()

    while voice_client.is_playing():
        await counter.add_timer() 
        if  await counter.get_time() > playing_now_duration:
            voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
            voice_client.stop()
            print("\n Timer excedeu o tempo da musica\n")      
        await asyncio.sleep(1)
        while voice_client.is_paused():
            await asyncio.sleep(1)
    
    if await counter.get_time() == 1: #Erro de forbideen ?
        print("\n ERRO FORBIDEN TIMER, musica "+queue[0]["title"]+"\n") 
        await call_next_song(client, ctx, queue, bot_info, counter)
        return False

    print(str(await counter.get_time()))
    print("Saiu loop\n")

    return True


async def call_next_song(client, ctx, queue, bot_info, counter):

    if not queue: return False
    guild = ctx.guild
    voice_client = discord.utils.get(client.voice_clients, guild=guild)
    
    if not voice_client: await join(ctx)
    await counter.reset()
    await play_next(client, ctx, queue, bot_info, counter)

    return True
    

async def query(args, ctx, queue):
    search_query = " ".join(args)
    await ctx.channel.send(":musical_note: **Searching** :mag_right: `" + search_query + "`")
    await search.query.query_play(ctx, search_query, queue)
