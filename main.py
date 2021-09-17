import discord
import os

client = discord.Client()
token = os.getenv("TOKEN")

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("yes")

client.run(os.getenv(token))


