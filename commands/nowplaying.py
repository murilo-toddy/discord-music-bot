import discord
from utils import embedded_message
from config import counter

async def nowplaying(client, ctx, queue):

    if len(queue) == 0:
        await embedded_message(ctx, "**Not Playing**", "_There's nothing playing at the moment_")
        return

    # Music information
    music_url = queue[0]["url"]
    music_title = queue[0]["title"]
    music_thumb = queue[0]["thumb"]
    
    username_request = queue[0]["user"]
    username_img_request = queue[0]["userAvatar"]

    music_duration = queue[0]["duration"]
    music_duration_seconds = queue[0]["duration_seconds"]
    music_current_time_seconds = await counter.get_time()
    music_current_time = format_time(music_current_time_seconds)
    progress_bar = ""

    total = 30
    number_before = int((music_current_time_seconds*total)//music_duration_seconds)
    number_after = total - number_before

    # Generates progress bar
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

    embed_var.set_footer(text=" Resquested by " + username_request, icon_url=username_img_request)
    embed_var.set_author(name='Now Playing 🎵',icon_url=client.user.avatar_url)
    embed_var.set_thumbnail(url=music_thumb)
    await ctx.channel.send(embed=embed_var)

 

def format_time(time):
   
    seconds = format_subtime(str(time % 60))
    
    # Time is less than an hour
    if time < 3600:
        minutes = format_subtime(str(time // 60))
        return minutes + ":" + seconds
    
    # Time is more than an hour
    minutes = format_subtime(str(time // 60 % 60))
    hours = format_subtime(str(time % 3600))
    return hours + ":" + minutes + ":" + seconds


def format_subtime(subtime):
    if len(subtime) == 0: return "00"
    elif len(subtime) == 1: return "0" + subtime
    else: return subtime

