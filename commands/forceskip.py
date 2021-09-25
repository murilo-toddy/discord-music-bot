from .play import play_next, ForceSkip
import discord


async def force_skip(client, ctx, queue):
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
   # await ForceSkip()
    voice_client.stop()
    await ShowMessage(ctx)

async def ShowMessage(ctx):
    await ctx.channel.send(":fast_forward: ***Skipped :mechanical_leg:***")

    
    