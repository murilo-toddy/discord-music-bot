from .play import change_loop

async def loop(ctx):
    bool_loop = await change_loop()
    await show_message(ctx, bool_loop)

async def show_message(ctx, bool_loop):
    if bool_loop:
        await ctx.channel.send(":repeat_one: **Enabled!**")
    else:
        await ctx.channel.send(":repeat_one: **Disabled!**")
   