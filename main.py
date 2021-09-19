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
import Comandos.log as _log


load_dotenv()

TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix='!')


########################################

queue = Lista()

########################################


@client.event
async def on_ready():
    print("\n [!] Bot iniciado.")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print("\n [!] Status do Bot modificado com sucesso.")



@client.command()
async def join(ctx):
    _log.log_function("join")
    await _join.join(ctx)


@client.command(aliases=["np"])
async def nowplaying(ctx):
    _log.log_function("nowplaying")
    await _nowplaying.nowplaying(client,ctx)


@client.command(aliases=["loopq", "lq"])
async def loopqueue(ctx):
    _log.log_function("loopqueue")
    await _loopqueue.loopqueue(client,ctx)


@client.command()
async def loop(ctx):
    _log.log_function("loop")
    await _loop.loop(client,ctx)


@client.command()
async def leave(ctx):
    _log.log_function("leave")
    await _leave.leave(client,ctx)


@client.command(brief="", aliases=["p"])
async def play(ctx, *url):
    _log.log_function("play")
    await _play.play(client, ctx, queue, *url)


@client.command()
async def pause(ctx):
    _log.log_function("pause")
    await _pause.pause(client, ctx)


@client.command()
async def resume(ctx):
    _log.log_function("resume")
    await _resume.resume(client, ctx)



if __name__ == '__main__':
    client.run(TOKEN)
