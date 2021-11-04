import discord

def set_video_info(ctx, response,queue):
    music_info = {}

    hours = minutes = seconds = duration = ""
    duration_in_seconds = 0
    
    try:
        duration = response["items"][0]["contentDetails"]["duration"][2:]
    except:
        print("\n\n [!] Video unavailable\n\n")
        return False

    if duration.find("H") != -1: [hours,duration] = duration.split("H")
    if duration.find("M") != -1: [minutes,duration] = duration.split("M")
    if duration.find("S") != -1: [seconds,duration] = duration.split("S")

    if hours != "":
        duration += hours + ":"
        duration_in_seconds += 60*60*int(hours)

    if minutes != "":
        if len(minutes) == 1: duration+="0"
        duration += minutes + ":"
        duration_in_seconds += 60*int(minutes)
    else:
        duration += "00:"

    if seconds != "":
        if len(seconds) == 1: duration += "0"
        duration+= seconds
        duration_in_seconds += int(seconds)
    else:
        duration += "00"

    music_info["title"] = response["items"][0]["snippet"]["title"]
    music_info["id"] = response["items"][0]["id"]
    music_info["url"] = "https://www.youtube.com/watch?v=" + music_info["id"]
    music_info["thumb"] = response["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
    music_info["duration"] = duration
    music_info["duration_seconds"] = duration_in_seconds
    music_info["user"] = ctx.message.author.name
    music_info["userAvatar"]= ctx.message.author.avatar_url

    queue.append(music_info)
    return True


async def show_message_playlist(musics, playlist_name, ctx):
    embed = discord.Embed(
        title = '**Playlist Enqueued! '+playlist_name+"**",
        description = f"Total `{musics}` musics were enqueued",
        color = discord.Color.red()
    )

    embed.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embed)


async def show_message_video(video_title, ctx, queue):

    if len(queue)==1:
        desc = f"[{video_title}]({queue[len(queue)-1]['url']}) was enqueued\n\nPlaying Now!"
    else:
        desc = f"[{video_title}]({queue[len(queue)-1]['url']}) was enqueued\n\nPosition in queue `{len(queue)-1}`"

    embedVar = discord.Embed(
        title = "**Video Enqueued!**",
        description = desc,
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embedVar)
    