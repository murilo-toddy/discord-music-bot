import discord
from discord.ext import commands
import os, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="!")
token = 'ODg4NTY4MjA4ODI1NjQ3MTA0.YUUloQ.2KrEmBYH6wp3E-6pfk14y9KWbKY'

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return   
#
#     if message.content.startswith("!hello"):
#         await message.channel.send("yes")

voice = discord.VoiceChannel

# @client.command(name="play")
# async def play(ctx):
#     voiceChannel = ctx.author.voice.channel
#     voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
#     # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     await voice.move_to(channel)

@client.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    voice = get(self.bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()    


# print (os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))


