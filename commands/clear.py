async def clear(ctx, queue):
    if len(queue) > 0:
        UrlAtual = queue[0]
        queue.remove(0)
        queue.clear()
        queue[0] = UrlAtual
    await ctx.channel.send("Queue cleared :mechanical_arm:")