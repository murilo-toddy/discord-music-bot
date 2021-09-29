from utils import embedded_message, get_time_in_seconds
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
