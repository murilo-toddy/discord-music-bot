import commands as cmd, asyncio
from .forceskip import force_skip

async def play_skip(client, ctx, queue, bot_info, counter, *url):
    size = len(queue)
    await cmd.play.play(client, ctx, queue, bot_info, counter, *url)
    if len(queue) > 1:
        await asyncio.sleep(1)
        if size < len(queue):
            await cmd.move.move_to(ctx, queue, size, 1)
            await force_skip(client,ctx,queue,bot_info)
    if len(queue) == 1:
        await asyncio.sleep(1)
        await force_skip(client,ctx,queue,bot_info)
    
        
        