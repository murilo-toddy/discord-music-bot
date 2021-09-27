import discord, os, json
from discord.voice_client import VoiceClient
from discord.ext import commands
from dotenv import load_dotenv

from data_structure import Queue

from verify_channel import verify_channel, verify_channel_play
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
client = commands.Bot(command_prefix="!", case_insensitive=True)


########################################

queue = Queue()

########################################


@client.event
async def on_ready():
    print("\n [!] Bot started.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print("\n [!] Bot Status updated successfully.")



@client.command(aliases=["j"])
async def join(ctx):
    log_function("join")
    if not await verify_channel(ctx, False): return
    await _join.join(ctx)


@client.command(aliases=["np"])
async def nowplaying(ctx):
    log_function("nowplaying")
    if not await verify_channel(ctx): return
    await _nowplaying.nowplaying(client,ctx,queue)


@client.command(aliases=["loopq", "lq","loop queue"])
async def loopqueue(ctx):
    log_function("loopqueue")
    if not await verify_channel(ctx): return
    await _loopqueue.loopqueue(ctx)


@client.command(aliases=["l"])
async def loop(ctx):
    log_function("loop")
    if not await verify_channel(ctx): return
    await _loop.loop(ctx)


@client.command(aliases=["dc","disconnect"])
async def leave(ctx):
    log_function("leave")
    if not await verify_channel(ctx): return
    await _leave.leave(ctx,queue)


@client.command(brief="Toca uma música maneira", aliases=["p"])
async def play(ctx, *url):
    log_function("play")
    if not await verify_channel_play(ctx): return
    await _play.play(client, ctx, queue, *url)


@client.command()
async def pause(ctx):
    log_function("pause")
    if not await verify_channel(ctx): return
    await _pause.pause(client, ctx)


@client.command()
async def resume(ctx):
    log_function("resume")
    if not await verify_channel(ctx): return
    await _resume.resume(client, ctx)


@client.command()
async def shuffle(ctx):
    log_function("shuffle")
    if not await verify_channel(ctx): return
    await _shuffle.shuffle(ctx, queue)


@client.command(aliases=["m"])
async def move(ctx, *args):
    log_function("move")
    if not await verify_channel(ctx): return
    await _move.move(ctx, queue, *args)


@client.command(aliases=["queue", "q"])
async def queue_(ctx):
    log_function("queue")
    if not await verify_channel(ctx): return
    await _queue.queue(ctx, queue,client)


@client.command(aliases=["r"])
async def remove(ctx, *args):
    log_function("remove")
    if not await verify_channel(ctx): return
    await _remove.remove(ctx, queue, *args)


@client.command(aliases=["fs", "skip", "s", "skp"])
async def forceskip(ctx):
    log_function("forceskip")
    if not await verify_channel(ctx): return
    await _forceskip.force_skip(client, ctx)


@client.command(aliases=["c","clean"])
async def clear(ctx):
    log_function("clear")
    if not await verify_channel(ctx): return
    await _clear.clear(ctx, queue)


@client.command()
async def seek(ctx):
    log_function("seek")
    await ctx.channel.send("Função ainda não implementada")



if __name__ == '__main__':
    client.run(TOKEN)


