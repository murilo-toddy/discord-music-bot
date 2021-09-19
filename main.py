import os, discord
from discord.voice_client import VoiceClient
from discord.ext import commands
from dotenv import load_dotenv

from EstruturaV2 import Lista

import Comandos.pause as _pause
import Comandos.resume as _resume
import Comandos.join as _join
import Comandos.play as _play
import Comandos.leave as _leave
import Comandos.forceskip as _forceskip
import Comandos.clear as _clear
import Comandos.loop as _loop
import Comandos.loopqueue as _loopqueue
import Comandos.nowplaying as _nowplaying
import Comandos.seek as _seek
import Comandos.shuffle as _shuffle


load_dotenv()

TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix='!')


########################################

queue = Lista()

########################################


@client.event
async def on_ready():
    print("\n [*] The bot is running.")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print("\n [*] The bot's status was successfully set.")



@client.command()
async def join(ctx):
    await _join.join(ctx)


# @client.command()
# async def clear(ctx):
#     await _clear.clear(queue)


@client.command()
async def leave(ctx):
    await _leave.leave(ctx)


@client.command(brief="", aliases=["p"])
async def play(ctx, *url):
    await _play.play(client, ctx, queue, *url)


@client.command()
async def pause(ctx):
    await _pause.pause(client, ctx)


@client.command()
async def resume(ctx):
    await _resume.resume(client, ctx)



if __name__ == '__main__':
    client.run(TOKEN)
