async def clear(ctx, queue):
    queue.clear()
    await ctx.channel.send("Queue cleared :mechanical_arm:")