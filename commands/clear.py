async def clear(ctx, queue):
    if len(queue) > 0:
        now_playing = queue[0]
        queue.remove(0)
        queue.clear()
        queue[0] = now_playing
    await ctx.channel.send("Fila limpa :mechanical_arm:")