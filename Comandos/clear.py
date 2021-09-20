async def clear(ctx, queue):
    queue.clear()
    await ctx.channel.send("fila limpada reizao daora")