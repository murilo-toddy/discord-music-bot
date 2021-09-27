async def verify_channel(ctx, sender_equals_bot: bool = True):
    sender = ctx.author.voice
    if not sender:
        await ctx.channel.send("Você deve estar conectado a um canal de voz")
        return False

    sender_channel = sender.channel
    if sender_equals_bot:
        if ctx.guild.voice_client:
            bot_channel = ctx.guild.voice_client.channel
            if bot_channel != sender_channel:
                await ctx.channel.send("Não aceito comando de estrangeiros! :ghost: ")
                return False
        else:
            await ctx.channel.send("***Not connected***")
            return False
    return True


async def verify_channel_play(ctx):
    Sender = ctx.author.voice
    if not Sender:
        await ctx.channel.send("Você deve estar conectado a um canal de voz")   
        return False

    sender_channel = Sender.channel
    bot_channel = ctx.guild.voice_client
    if bot_channel:
        if not bot_channel.channel == sender_channel:
            await ctx.channel.send("Não aceito comando de estrangeiros! :ghost: ")
            return False
        else:
            return True

    await ctx.channel.send(":wave: ***Hello Hello***")
    await ctx.author.voice.channel.connect()
    bot_channel = ctx.guild.voice_client
    bot_channel.pause()
    return True