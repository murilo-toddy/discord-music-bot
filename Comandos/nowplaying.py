import sys, discord
from typing import Text
from discord.colour import Color
import collections

from .play import GetCurrentURL

sys.path.append("..")

from youtube import get_video_data

async def nowplaying(client,ctx):
    url = await GetCurrentURL()
    info = await get_video_data(url)
    await ShowMessage(client,ctx,info)

async def ShowMessage(client,ctx,info):

    url_musica= str(info["url"])
    titulo_musica = str(info["title"])

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
        description = "\n["+titulo_musica +"]("+ url_musica+") \n\n**"+ProgressBar+"**\n\n"+str(NumberBefore)+"/"+str(Total),
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    embedVar.set_author(name='Now Playing 🎵',icon_url= client.user.avatar_url)
    embedVar.set_thumbnail(url = client.user.avatar_url) #Change to thumbnail
    await ctx.channel.send(embed = embedVar)

 