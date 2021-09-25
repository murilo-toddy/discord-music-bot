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
client = commands.Bot(command_prefix="!", case_insensitive=True)


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
    if not await verify_channel(ctx, False):
        return
    log_function("join")
    await _join.join(ctx)


@client.command(aliases=["np"])
async def nowplaying(ctx):
    if not await verify_channel(ctx):
        return
    log_function("nowplaying")
    await _nowplaying.nowplaying(client,ctx,queue)


@client.command(aliases=["loopq", "lq","loop queue"])
async def loopqueue(ctx):
    if not await verify_channel(ctx):
        return
    log_function("loopqueue")
    await _loopqueue.loopqueue(client,ctx)


@client.command(aliases=["l"])
async def loop(ctx):
    if not await verify_channel(ctx):
        return
    log_function("loop")
    await _loop.loop(client,ctx)


@client.command(aliases=["dc","disconnect"])
async def leave(ctx):
    if not await verify_channel(ctx):
        return
    log_function("leave")
    await _leave.leave(ctx,queue)


@client.command(brief="", aliases=["p"])
async def play(ctx, *url):
    if not await verify_channel_play(ctx):
        return
    log_function("play")
    await _play.play(client, ctx, queue, *url)


@client.command()
async def pause(ctx):
    if not await verify_channel(ctx):
        return
    log_function("pause")
    await _pause.pause(client, ctx)


@client.command()
async def resume(ctx):
    if not await verify_channel(ctx):
        return
    log_function("resume")
    await _resume.resume(client, ctx)


@client.command()
async def shuffle(ctx):
    if not await verify_channel(ctx):
        return
    log_function("shuffle")
    await _shuffle.shuffle(ctx, queue)


@client.command(aliases=["m"])
async def move(ctx, *args):
    if not await verify_channel(ctx):
        return
    log_function("move")
    print(args)
    await _move.move(ctx, queue, *args)


@client.command(aliases=["queue", "q"])
async def queue_(ctx):
    if not await verify_channel(ctx):
        return
    log_function("queue")
    await _queue.queue(ctx, queue)


@client.command(aliases=["r"])
async def remove(ctx, *args):
    if not await verify_channel(ctx):
        return
    log_function("remove")
    await _remove.remove(ctx, queue, *args)


@client.command(aliases=["fs", "skip", "s", "skp"])
async def forceskip(ctx):
    if not await verify_channel(ctx):
        return
    log_function("forceskip")
    await _forceskip.force_skip(client, ctx, queue)

@client.command(aliases=["c","clean"])
async def clear(ctx):
    if not await verify_channel(ctx):
        return
    log_function("clear")
    await _clear.clear(ctx, queue)



async def verify_channel(ctx, sender_equals_bot: bool = True):
    sender = ctx.author.voice
    if not sender:
        await ctx.channel.send("You must be connected to a voice channel")
        return False

    sender_channel = sender.channel
    if sender_equals_bot:
        if ctx.guild.voice_client:
            bot_channel = ctx.guild.voice_client.channel
            if bot_channel != sender_channel:
                await ctx.channel.send("Não aceito comandos de estrangeiros! :ghost: ")
                return False
        else:
            await ctx.channel.send("***Not connected***")
            return False
    return True



async def verify_channel_play(ctx):
    Sender = ctx.author.voice
    if not Sender:
        await ctx.channel.send("Precisa estar conectado")   
        return False

    sender_channel = Sender.channel
    bot_channel = ctx.guild.voice_client
    if bot_channel:
        if not bot_channel.channel == sender_channel:
            await ctx.channel.send("Não aceito comandos de estrangeiros! :ghost: ")
            return False
        else:
            return True

    await ctx.channel.send(":wave: ***Hello Hello***")
    await ctx.author.voice.channel.connect()
    bot_channel = ctx.guild.voice_client
    bot_channel.pause()
    return True



if __name__ == '__main__':
    client.run(TOKEN)


