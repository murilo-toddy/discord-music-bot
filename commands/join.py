async def join(ctx):

    if ctx.guild.voice_client:
        await ctx.channel.send("**Já estou conectado**")
    
    else:
        await ctx.channel.send(":wave: **Hello Hello**")
        await ctx.author.voice.channel.connect()
        bot_channel = ctx.guild.voice_client
        bot_channel.pause()