from .play import change_loop_queue

async def loopqueue(ctx):
    loop_queue = await change_loop_queue()
    await show_message(ctx, loop_queue)

async def show_message(ctx, loop_queue):
    if loop_queue:
        await ctx.channel.send(":repeat: **Queue loop enabled!**")
    else:
        await ctx.channel.send(":repeat: **Queue loop Disabled!**")