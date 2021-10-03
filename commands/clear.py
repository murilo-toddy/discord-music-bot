from utils import embedded_message

# Removes all songs from queue
async def clear(ctx, queue):
    if len(queue) > 0:
        now_playing = queue[0]
        queue.remove(0)
        queue.clear()
        queue[0] = now_playing
    await embedded_message(ctx, "**Cleared :mechanical_arm:**", "_The queue is now empty_")
    