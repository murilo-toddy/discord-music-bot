import log

async def leave(ctx):
    log.log_function("leave")

    voice = ctx.guild.voice_client

    if voice:
        await ctx.channel.send("To de saidas")
        await ctx.voice_client.disconnect()

    else:
        await ctx.channel.send("Não to conectado")
