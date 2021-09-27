import discord

async def force_skip(client, ctx):
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice_client.stop()
    await ShowMessage(ctx)

async def ShowMessage(ctx):
    await ctx.channel.send(":fast_forward: ***Pulado :mechanical_leg:***")

    
    