import asyncio, discord

async def embedded_message(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        color = discord.Color.red()
    )

    embed.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embed)


class Counter:
    def __init__(self):
        self.counter = 0

    async def start_timer(self):
        while True:
            await asyncio.sleep(1)
            self.counter += 1
    
    async def reset(self):
        self.counter = 0

    async def get_time(self):
        return self.counter