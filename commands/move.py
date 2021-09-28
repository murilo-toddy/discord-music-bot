import discord

async def move(ctx, queue, *args):
    if len(args) == 0:
        await ctx.channel.send("Você precisa fornecer uma posição :japanese_goblin:")
    
    elif len(args) == 1:
        await move_to(ctx, queue, args[0], 1)

    elif len(args) == 2:
        await move_to(ctx, queue, args[0], args[1])

    else:
        await ctx.channel.send("Sintaxe incorreta :japanese_goblin:")



async def move_to(ctx, queue, pos1, pos2):
    try:
        pos1 = int(pos1)
        pos2 = int(pos2)
    
    except:
        await ctx.channel.send("O argumento precisa ser um número válido :japanese_goblin:")
        print(" [!!] Error in \'move\' function\n      * Could not convert position!")
        return

        
    if pos1 > (len(queue) + 1) or pos2 > (len(queue) + 1) and pos1 != 0 and pos2 != 0:
        await ctx.channel.send("Posição inválida :japanese_goblin:")
        return

    title = queue[pos1]["title"]
    queue.move(pos1, pos2)
    await send_message(ctx, title, pos1, pos2)



async def send_message(ctx, title, starting_position, final_position):

    embedVar = discord.Embed(
        title = "**Moved!**",
        description ="Changed `"+str(title)+"` position from `"+str(starting_position)+"` to `"+str(final_position)+"`",
        color = discord.Color.red()
    )

    embedVar.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embedVar)