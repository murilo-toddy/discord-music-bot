import asyncio
import discord

counter = 0

async def create_counter():
    global counter
    while True:
        await asyncio.sleep(1)
        counter += 1

async def reset_timer():
    global counter
    counter = 0

async def get_time():
    global counter
    return counter




async def embedded_message(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        color = discord.Color.red()
    )

    embed.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embed)