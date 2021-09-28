import discord
from utils import embedded_message, get_time

async def nowplaying(client, ctx, queue):

    if len(queue) == 0:
        await embedded_message(ctx, "**Not Playing**", "_There's nothing playing at the moment")
        return

    music_url= queue[0]["url"]
    music_title = queue[0]["title"]
    music_thumb = queue[0]["thumb"]
    music_duration = queue[0]["duration"]
    username_request = queue[0]["user"]
    username_img_request = queue[0]["userAvatar"]

    music_duration = 10
    music_current_time = await get_time()
    progress_bar = ""

    total = 30
    number_before = int((music_current_time/music_duration)*total)
    number_after = total - number_before

    for i in range(number_before):
        progress_bar += "-"

    progress_bar +='🔘'

    for i in range(number_after):
        progress_bar += "-"

    embed_var = discord.Embed(
        title = '',
        description = "\n["+music_title +"]("+ music_url+") \n\n**"+progress_bar+"**\n\n"+"`"+str(music_current_time)
                        +"/"+music_duration+"`",
        color = discord.Color.red()
    )

    embed_var.set_footer(text= " Resquested by " + username_request, icon_url= username_img_request)
    embed_var.set_author(name='Now Playing 🎵',icon_url= client.user.avatar_url)
    embed_var.set_thumbnail(url = music_thumb) #Change to thumbnail
    await ctx.channel.send(embed = embed_var)

 