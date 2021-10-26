import commands as cmd, asyncio

async def play_now(client, ctx, queue, bot_info, counter, *url):
    size = len(queue)
    await cmd.play.play(client, ctx, queue, bot_info, counter, *url)
    if len(queue) > 1:
        await asyncio.sleep(1)
        if size < len(queue):
            await cmd.move.move_to(ctx, queue, size, 1)