from .play import play_next
import discord


async def force_skip(client, ctx, queue):
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice_client.pause()

    await ctx.channel.send("sera skipado rei")
    await play_next(client, ctx, queue)
    