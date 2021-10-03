from utils import embedded_message

# Shuffles queue
async def shuffle(ctx, queue):
    if len(queue) > 0:
        now_playing = queue[0]
        queue.remove(0)
        queue.shuffle()
        queue[0] = now_playing
        await embedded_message(ctx, ":twisted_rightwards_arrows: **Shuffled**", "_The queue has been shuffled_")
    
    else:
        await embedded_message(ctx, ":exclamation: **Empty Queue**", "_Nothing to shuffle_")
        