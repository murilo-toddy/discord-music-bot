async def shuffle(ctx, queue):
    if len(queue) > 0:
        now_playing = queue[0]
        queue.remove(0)
        queue.shuffle()
        queue[0] = now_playing
        await ctx.channel.send("**Fila embaralhada** :ok_hand:")
    
    else:
        await ctx.channel.send("***Fila vazia***")