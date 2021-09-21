from .play import ChangeLoopQueue

async def loopqueue(client, ctx):
    boolLoopQueueu = await ChangeLoopQueue()
    await ShowMessage(ctx,boolLoopQueueu)

async def ShowMessage(ctx,boolLoopQueueu):
    if boolLoopQueueu:
        await ctx.channel.send(":repeat: **Queue loop enabled!**")
    else:
        await ctx.channel.send(":repeat: **Queue loop Disabled!**")