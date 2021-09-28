import discord
from utils import embedded_message
from config import counter

async def nowplaying(client, ctx, queue):

    if len(queue) == 0:
        await embedded_message(ctx, "**Not Playing**", "_There's nothing playing at the moment_")
        return

    music_url = queue[0]["url"]
    music_title = queue[0]["title"]
    music_thumb = queue[0]["thumb"]
    
    username_request = queue[0]["user"]
    username_img_request = queue[0]["userAvatar"]

    music_duration = queue[0]["duration"]
    music_current_time_seconds = await counter.get_time()

    music_duration_seconds = format_to_seconds(music_duration)
    music_current_time = format_to_time(music_current_time_seconds)
    progress_bar = ""

    total = 30
    number_before = int((music_current_time_seconds/music_duration_seconds)*total)
    number_after = total - number_before

    for i in range(number_before):
        progress_bar += "-"

    progress_bar +='🔘'

    for i in range(number_after):
        progress_bar += "-"

    embed_var = discord.Embed(
        title = '',
        description = "\n["+music_title +"]("+ music_url+") \n\n**"+progress_bar+"**\n\n"+"`"+music_current_time
                        +"/"+music_duration+"`",
        color = discord.Color.red()
    )

    embed_var.set_footer(text= " Resquested by " + username_request, icon_url= username_img_request)
    embed_var.set_author(name='Now Playing 🎵',icon_url= client.user.avatar_url)
    embed_var.set_thumbnail(url = music_thumb) #Change to thumbnail
    await ctx.channel.send(embed = embed_var)

 

def format_to_time(time):
    minutes = str(time // 60)
    if len(minutes) == 0: minutes = "00"
    if len(minutes) == 1: minutes = "0" + minutes
    seconds = str(time % 60)
    if len(seconds) == 1: seconds = "0" + seconds
    
    return minutes + ":" + seconds


def format_to_seconds(time):
    strsize = len(time)
    seconds = int(time[strsize-2:])
    minutes = int(time[strsize-5:strsize-3])
    return 60 * minutes + seconds