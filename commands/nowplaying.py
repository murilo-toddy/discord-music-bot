import sys, discord
from typing import Text
from discord.colour import Color

sys.path.append("..")

async def nowplaying(client,ctx,queue):

    if len(queue) == 0:
        await ctx.channel.send("**Nothing playing**")
        return

    url_musica= queue[0]["url"]
    titulo_musica = queue[0]["title"]
    UserNameRequest = queue[0]["user"]
    ImgNameRequest = queue[0]["userAvatar"]
    MusicThumb = queue[0]["thumb"]
    MusicDuration = queue[0]["duration"]

    music_current_time = 10
    music_duration = 90

    ProgressBar = ""

    Total=30
    NumberBefore = int( (music_current_time/music_duration)*Total )
    NumberAfter = Total - NumberBefore

    for i in range(NumberBefore):
        ProgressBar += "-"

    ProgressBar +='🔘'

    for i in range(NumberAfter):
        ProgressBar += "-"


    embedVar = discord.Embed(
        title = '',
        description = "\n["+titulo_musica +"]("+ url_musica+") \n\n**"+ProgressBar+"**\n\n"+"`music_current_time/"+MusicDuration+"`",
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + UserNameRequest, icon_url= ImgNameRequest)
    embedVar.set_author(name='Now Playing 🎵',icon_url= client.user.avatar_url)
    embedVar.set_thumbnail(url = MusicThumb) #Change to thumbnail
    await ctx.channel.send(embed = embedVar)

 