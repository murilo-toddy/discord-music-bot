async def leave(ctx,queue):

    voice = ctx.guild.voice_client

    if len(queue)>0:
        queue.clear()

    if voice:
        await ctx.channel.send("**Bye Bye** :call_me:")
        await ctx.voice_client.disconnect()

    else:
        await ctx.channel.send("**Not connected**")
