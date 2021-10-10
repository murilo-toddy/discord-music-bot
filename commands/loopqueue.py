from utils import embedded_message

# Loops a whole queue
async def loopqueue(ctx, bot_info):
    loop_queue = bot_info.change_loop_queue()
    await show_message(ctx, loop_queue)

async def show_message(ctx, loop_queue):
    if loop_queue:
        await embedded_message(ctx, ":repeat: **Enabled**", "_Loop Queue is now enabled!_")
    else:
        await embedded_message(ctx, ":repeat: **Disabled**", "_Loop Queue is now disabled!_")
        