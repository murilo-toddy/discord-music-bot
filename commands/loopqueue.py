from .play import change_loop_queue
from utils import embedded_message

# Loops a whole queue
async def loopqueue(ctx):
    loop_queue = await change_loop_queue()
    await show_message(ctx, loop_queue)

async def show_message(ctx, loop_queue):
    if loop_queue:
        await embedded_message(ctx, ":repeat_one: **Enabled**", "_Loop Queue is now enabled!_")
    else:
        await embedded_message(ctx, ":repeat_one: **Disabled**", "_Loop Queue is now disabled!_")