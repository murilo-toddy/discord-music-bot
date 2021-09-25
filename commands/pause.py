import discord

async def pause(client, ctx):
    voice_client:  discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await ctx.channel.send("**Not connected**")
    
    elif not voice_client.is_playing() or voice_client.is_paused():
        await ctx.channel.send("**Not playing**")

    else:
        voice_client.pause()
        await ctx.channel.send("**Paused** :shushing_face:")