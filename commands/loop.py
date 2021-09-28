from .play import change_loop
from utils import embedded_message

# Loops a single song
async def loop(ctx):
    loop = await change_loop()
    await show_message(ctx, loop)

async def show_message(ctx, loop):
    if loop:
        await embedded_message(ctx, ":repeat_one: **Enabled**", "_Loop is now enabled!_")
    else:
        await embedded_message(ctx, ":repeat_one: **Disabled**", "_Loop is now disabled!_")
   