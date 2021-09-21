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
import Comandos.queue as _queue
import Comandos.move as _move
import Comandos.remove as _remove


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



@client.command(aliases=["j"])
async def join(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("join")
    await _join.join(ctx)


@client.command(aliases=["np"])
async def nowplaying(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("nowplaying")
    await _nowplaying.nowplaying(client,ctx)


@client.command(aliases=["loopq", "lq","loop queue"])
async def loopqueue(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("loopqueue")
    await _loopqueue.loopqueue(client,ctx)


@client.command(aliases=["l"])
async def loop(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("loop")
    await _loop.loop(client,ctx)


@client.command(aliases=["dc","disconnect"])
async def leave(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("leave")
    await _leave.leave(ctx,queue)


@client.command(brief="", aliases=["p","P"])
async def play(ctx, *url):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("play")
    await _play.play(client, ctx, queue, *url)


@client.command()
async def pause(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("pause")
    await _pause.pause(client, ctx)


@client.command()
async def resume(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("resume")
    await _resume.resume(client, ctx)


@client.command()
async def shuffle(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("shuffle")
    await _shuffle.shuffle(ctx, queue)


@client.command(aliases=["m"])
async def move(ctx, *args):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("move")
    print(args)
    await _move.move(ctx, queue, *args)


@client.command(aliases=["queue", "q"])
async def queue_(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("queue")
    await _queue.queue(ctx, queue)


@client.command(aliases=["r"])
async def remove(ctx, *args):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("remove")
    await _remove.remove(ctx, queue, *args)


@client.command(aliases=["fs", "skip", "s", "skp"])
async def forceskip(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("forceskip")
    await _forceskip.force_skip(client, ctx, queue)

@client.command(aliases=["c","clean"])
async def clear(ctx):
    if not await VerificaCanal(ctx):
        return
    _log.log_function("clear")
    await _clear.clear(ctx, queue)


async def VerificaCanal(ctx):
    if not ctx.author.voice:
        await ctx.channel.send("Não aceito comandos de estrangeiros! :ghost: ")
        return False
    else:
        return True


if __name__ == '__main__':
    client.run(TOKEN)


