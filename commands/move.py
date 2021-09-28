import discord

async def move(ctx, queue, *args):
    if len(args) == 0:
        await ctx.channel.send("Você precisa fornecer uma posição :japanese_goblin:")
    
    elif len(args) == 1:
        try:
            pos = int(args[0])

        except:
            await ctx.channel.send("O argumento precisa ser um número válido :japanese_goblin:")
            return

        if pos > (len(queue)+1) and pos !=0:
            await ctx.channel.send("Posição inválida :japanese_goblin:")
            return

        title = queue[pos]["title"]
        queue.move((pos),1)
        await send_message(ctx, title, pos)
            


    elif len(args) == 2:
        try:
            pos1 = int(args[0])
            pos2 = int(args[1])
            
            if pos1 > (len(queue)+1) or pos2 > (len(queue)+1) and pos1!=0 and pos2 !=0:
                await ctx.channel.send("Posição inválida :japanese_goblin:")
                return

            title = queue[pos1]["title"]
            queue.move((pos1),pos2)
            await send_message(ctx,title,pos1,pos2)

        except:
            await ctx.channel.send("O argumento precisa ser um número válido :japanese_goblin:")

    else:
        await ctx.channel.send("Sintaxe incorreta :japanese_goblin:")


async def send_message(ctx, title, starting_position, final_position=1):

    embedVar = discord.Embed(
        title = "**Moved!**",
        description ="Changed `"+str(title)+"` position from `"+str(starting_position)+"` to `"+str(final_position)+"`",
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embedVar)
