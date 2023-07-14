import discord
from utils import embedded_message, format_time


async def nowplaying(client, ctx, queue, counter):

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

    total = 30
    number_before = int((music_current_time_seconds*total)//music_duration_seconds)
    number_after = total - number_before
    progress_bar = number_before * "-" + '🔘' + number_after * "-"

    embed_var = discord.Embed(
        title='',
        description=f"\n[{music_title}]({music_url}) \n\n**{progress_bar}**\n\n`{music_current_time}/{music_duration}`",
        color=discord.Color.red()
    )

    embed_var.set_footer(text=" Resquested by " + username_request, icon_url=username_img_request)
    embed_var.set_author(name='Now Playing 🎵', icon_url=client.user.avatar)
    embed_var.set_thumbnail(url=music_thumb)
    await ctx.channel.send(embed=embed_var)
