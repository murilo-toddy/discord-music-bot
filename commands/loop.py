from .play import ChangeLoop


async def loop(client, ctx):
    boolLoop = await ChangeLoop()
    await ShowMessage(ctx,boolLoop)

async def ShowMessage(ctx,boolLoop):
    if boolLoop:
        await ctx.channel.send(":repeat_one: **Enabled!**")
    else:
        await ctx.channel.send(":repeat_one: **Disabled!**")
   