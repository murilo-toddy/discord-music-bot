import sys, discord
from typing import Text
from discord.colour import Color

from .play import GetCurrentURL, GetMusicName

sys.path.append("..")

async def nowplaying(client,ctx):
    url = await GetCurrentURL()
    name =  await GetMusicName()
    await ShowMessage(client,ctx,url,name)

async def ShowMessage(client,ctx,url,name):

    url_musica= url
    titulo_musica = name

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

 