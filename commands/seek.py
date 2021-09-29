from data_structure import BotInfo
import ssl
from .play import FFMPEG_OPTIONS, play_next
from utils import embedded_message
from config import bot_info
import discord

# Skips to specific part of the music
async def seek(client, ctx, queue, *args):
    
    if len(args) == 0:
        await embedded_message(ctx, "**Invalid Syntax**", "You must specify a time!\nLike !seek `1:20` or !seek `80`")
        return
    
    elif len(args) > 1:
        await embedded_message(ctx, "**Invalid Syntax**", "Function only recieves one parameter!\nLike !seek `1:20` or !seek `80`")
        return

    time_seconds = get_time_in_seconds(str(args[0]))
    
    if not time_seconds and time_seconds != 0:
        print(" [!!] Error in \'seek\'\n      * Could not convert time")
        await embedded_message(ctx, "**Invalid Syntax**", "Time must be in seconds or hh:mm:ss format!\nLike !seek `1:20` or !seek `80`")
        return

    if len(queue) < 1:
        await embedded_message(ctx, "**Empty Queue**", "You cannot use this command\nin an empty queue")

    if time_seconds >= queue[0]["duration_seconds"]:
        await embedded_message(ctx, "**Invalid Time**  :nose:", "Time must be less than music duration!")
        return

    bot_info.seek_set_true(time_seconds)
    discord.utils.get(client.voice_clients, guild=ctx.guild).stop()    
    await embedded_message(ctx, ":orangutan:  **Seeked!**", "_Music time set to_ `" + args[0] + "`")



def get_time_in_seconds(time):

    # Only seconds
    try:
        time = int(time)
        return time
    
    # hh:mm:ss format
    except:
        time_size = len(time)
        try:
            seconds = int(time[time_size-2:])
            if time_size == 4: minutes = int(time[time_size-4])
            else: minutes = int(time[time_size-5:time_size-3])
            time_in_secs = 60 * minutes + seconds
            
            # mm:ss format
            if time_size < 6:
                return time_in_secs
            
            # hh:mm:ss format
            if time_size == 7: hours = int(time[time_size-7])
            else: hours = int(time[time_size-8:time_size-6])
            return 60*60*hours + time_in_secs
        
        except:
            print(" [!!] Error in \'seek\'\n      * Could not convert number to seconds")
            return None