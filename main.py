import os, discord
from discord.voice_client import VoiceClient
from discord.ext import commands
from dotenv import load_dotenv

from EstruturaV2 import Lista

from commands.log import log_function

import commands.pause as _pause
import commands.resume as _resume
import commands.join as _join
import commands.play as _play
import commands.leave as _leave
import commands.forceskip as _forceskip
import commands.clear as _clear
import commands.loop as _loop
import commands.loopqueue as _loopqueue
import commands.nowplaying as _nowplaying
import commands.seek as _seek
import commands.shuffle as _shuffle
import commands.queue as _queue
import commands.move as _move
import commands.remove as _remove


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
    log_function("join")
    await _join.join(ctx)


@client.command(aliases=["np"])
async def nowplaying(ctx):
    log_function("nowplaying")
    await _nowplaying.nowplaying(client,ctx)


@client.command(aliases=["loopq", "lq"])
async def loopqueue(ctx):
    log_function("loopqueue")
    await _loopqueue.loopqueue(client,ctx)


@client.command()
async def loop(ctx):
    log_function("loop")
    await _loop.loop(client,ctx)


@client.command()
async def leave(ctx):
    log_function("leave")
    await _leave.leave(ctx)


@client.command(brief="", aliases=["p"])
async def play(ctx, *url):
    log_function("play")
    await _play.play(client, ctx, queue, *url)


@client.command()
async def pause(ctx):
    log_function("pause")
    await _pause.pause(client, ctx)


@client.command()
async def resume(ctx):
    log_function("resume")
    await _resume.resume(client, ctx)


@client.command()
async def shuffle(ctx):
    log_function("shuffle")
    await _shuffle.shuffle(ctx, queue)


@client.command(aliases=["m"])
async def move(ctx, *args):
    log_function("move")
    print(args)
    await _move.move(ctx, queue, *args)


@client.command(aliases=["queue", "q"])
async def queue_(ctx):
    log_function("queue")
    await _queue.queue(ctx, queue)


@client.command(aliases=["r"])
async def remove(ctx, *args):
    log_function("remove")
    await _remove.remove(ctx, queue, *args)


@client.command(aliases=["fs", "skip", "s", "skp"])
async def forceskip(ctx):
    log_function("forceskip")
    await _forceskip.force_skip(client, ctx, queue)

@client.command(aliases=["c"])
async def clear(ctx):
    log_function("clear")
    await _clear.clear(ctx, queue)



if __name__ == '__main__':
    client.run(TOKEN)
