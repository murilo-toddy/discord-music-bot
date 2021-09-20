async def queue(ctx, queue):
    for item in queue:
        await ctx.channel.send(str(item))