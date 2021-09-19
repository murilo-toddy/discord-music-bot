import discord, log

async def pause(client, ctx):
    
    log.log_function("pause")
    
    voice_client:  discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await ctx.channel.send("Nao to conectado")
    
    elif not voice_client.is_playing() or voice_client.is_paused():
        await ctx.channel.send("nao to tocando")

    else:
        voice_client.pause()
        await ctx.channel.send("Pausado pattern")