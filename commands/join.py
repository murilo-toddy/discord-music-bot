async def join(ctx):
    bot_channel = ctx.guild.voice_client

    if bot_channel:
        await ctx.channel.send("**Já estou conectado**")
    
    else:
        await ctx.channel.send(":wave: **Hello Hello**")
        await ctx.author.voice.channel.connect()
        bot_channel = ctx.guild.voice_client
        bot_channel.pause()