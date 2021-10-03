import discord
from utils import embedded_message

async def pause(client, ctx):
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if not voice_client:
        await embedded_message(ctx, ":exclamation: **Not Connected**", "I'm currently not connected")
    
    elif not voice_client.is_playing() or voice_client.is_paused():
        await embedded_message(ctx, "**Not Playing**", "I am not playing, nerdola")

    else:
        voice_client.pause()
        await embedded_message(ctx, "**Paused** :shushing_face:", "_Current music paused_")
        