async def remove(ctx, queue, *args):
    if len(args) == 0:
        await ctx.channel.send("You must specify a position.")

    elif len(args) == 1:
        try:
            pos = int(*args[0])
        except:
            await ctx.channel.send("Argument must be a valid number.")
            return

        if pos > (len(queue)+1) and pos !=0:
            await ctx.channel.send("Invalid index.")
            return

        url = queue.remove(pos)
        await ctx.channel.send("Item " + str(url) + " successfully removed.") 
    
    else:
        await ctx.channel.send("Bad syntax.")

