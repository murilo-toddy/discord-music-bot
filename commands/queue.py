async def queue(ctx, queue):
    for i in range(len(queue)):
        if i != 0:
            await ctx.channel.send(str(queue[i]))