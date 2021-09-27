from .play import ChangeLoopQueue

async def loopqueue(ctx):
    loop_queue = await ChangeLoopQueue()
    await ShowMessage(ctx, loop_queue)

async def ShowMessage(ctx, loop_queue):
    if loop_queue:
        await ctx.channel.send(":repeat: **Queue loop enabled!**")
    else:
        await ctx.channel.send(":repeat: **Queue loop Disabled!**")