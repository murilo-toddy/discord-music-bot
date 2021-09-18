import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return   

#     if message.content.startswith("!hello"):
#         await message.channel.send("yes")


@client.command()
async def print(ctx, arg):
    await ctx.channel.send("aaaaa")


@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, url : str):
    await ctx.channel.send(arg)



client.run(TOKEN)


