import discord

async def resume(client, ctx):
    print('\n [*] \'!resume\' command called.')

    voice_client:  discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await ctx.channel.send("nao to conectado")

    elif voice_client.is_playing() or not voice_client.is_paused():
        await ctx.channel.send("nao to pausado")
    
    else:
        voice_client.resume()
        await ctx.channel.send("vortei")