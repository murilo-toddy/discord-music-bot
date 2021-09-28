import discord
from utils import embedded_message

# Skips playing song
async def force_skip(client, ctx):
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice_client.stop() # Stops so play_next gets called in play module
    await embedded_message(ctx, "**Skipped**", ":fast_forward: _Song Skipped_")