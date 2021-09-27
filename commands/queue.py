from typing import Text
import discord
from discord.colour import Color
import asyncio
import math

async def queue(ctx, queue,client):
    if(len(queue))<=1:
        await ctx.channel.send("***Fila vazia***")
        return

    TamanhoJ = math.ceil(len(queue)/10)

    Paginas = []
    for j in range(TamanhoJ):
        print(j)
        desc = ""
        for i in range(10):
            if i+j != 0 and i<len(queue):
                desc += str(i+j*10) +" - ["+str(queue[i+j*10]["title"] +"]("+str(queue[i+j*10]["url"])+")"+ " `"+str(queue[i+j*10]["duration"])+"` ("+str(queue[i+j*10]["user"]))+")\n"

        Pag = discord.Embed(
            title = "**Queue Songs!  Total = `"+str(len(queue)-1)+"` **",
            description = desc+"\n`"+str(j+1)+"/"+str(TamanhoJ)+"`",
            color = discord.Color.red()
        )

        Pag.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
        Pag.set_thumbnail(url = queue[0]["thumb"]) #Change to thumbnail
        Paginas.append(Pag)
    
    await PrintPaginas(ctx,Paginas,client)

async def PrintPaginas(ctx,Paginas,client):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    current = 0
    client.help_pages = Paginas
    msg = await ctx.send(embed=client.help_pages[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            embeded = client.help_pages[current]
            await msg.clear_reactions()

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(client.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(client.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=client.help_pages[current])