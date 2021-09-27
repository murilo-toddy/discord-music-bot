import discord

async def resume(client, ctx):

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await ctx.channel.send("**Não conectado**")

    elif voice_client.is_playing() or not voice_client.is_paused():
        await ctx.channel.send("I am already playing Nerdola")
    
    else:
        voice_client.resume()
        await ctx.channel.send("**Resumed** :face_in_clouds:")