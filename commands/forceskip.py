import discord
from utils import embedded_message

# Skips playing song
async def force_skip(client, ctx,queue,bot_info):

    if not queue:
        await embedded_message(ctx, "**Empty Player**", "_There is nothing playing_")
        return

    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice_client.stop() # Stops so play_next gets called in play module

    if bot_info.get_loop():
        if bot_info.get_loop_queue():
            if len(queue) > 0:
                next_song = queue[0]
                queue.remove(0)
                queue.append(next_song)
        elif len(queue) > 0:
            queue.remove(0)

    await embedded_message(ctx, "**Skipped**", ":fast_forward: _Song Skipped_")
    