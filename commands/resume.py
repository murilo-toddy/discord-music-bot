import discord
from utils import embedded_message

async def resume(client, ctx):

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await embedded_message(ctx, "**Not Connected**", ":exclamation: _I'm currently not connected_")

    elif voice_client.is_playing() or not voice_client.is_paused():
        await embedded_message(ctx, "**Already Playing**", "_I am already playing, nerdola_")
    
    else:
        voice_client.resume()
        await embedded_message(ctx, "**Resumed** :face_in_clouds:", "Current music resumed")
        