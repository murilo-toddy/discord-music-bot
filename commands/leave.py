async def leave(ctx,queue):
    
    if len(queue)>0:
        queue.clear()

    if ctx.guild.voice_client:
        await ctx.channel.send("**Bye Bye** :call_me:")
        await ctx.voice_client.disconnect()

    else:
        await ctx.channel.send("**Não estou conectado**")
