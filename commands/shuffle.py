async def shuffle(ctx, queue):
    if len(queue) > 0:
        UrlAtual = queue[0]
        queue.remove(0)
        queue.shuffle()
        queue[0] = UrlAtual
    await ctx.channel.send("**Shuffled queue** :ok_hand:")