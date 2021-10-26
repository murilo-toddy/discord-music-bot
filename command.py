from config import *
from utils import *
import commands as cmd
from commands.log import log_function

available_commands = {
    "help": [],
    "clear": ["c"],
    "credits": ["creditos", "créditos", "autores"],
    "forceskip": ["fs", "skip", "s", "skp", "next"],
    "join": ["j"],
    "leave": ["dc", "disconnect"],
    "loop": ["l"],
    "loopqueue": ["loopq", "lq"],
    "lyrics": ["ly"],
    "move": ["m", "mv"],
    "nowplaying": ["np"],
    "pause": [],
    "play": ["p"],
    "playnow": ["pn"],
    "playskip": ["ps"],
    "queue": ["queue", "q"],
    "remove": ["r"],
    "resume": ["continue"],
    "search": ["se", "srch", "busca", "choose"],
    "seek": [],
    "shuffle": []
}

async def function_check(ctx, function: str, check=True):
    log_function(function, ctx)
    if not await verify_channel(ctx, check): return None
    return bot.server[f"{ctx.guild.id}"]

async def function_check_play(ctx, function: str):
    log_function(function, ctx)
    if not await verify_channel_play(ctx): return None
    return bot.server[f"{ctx.guild.id}"]


@client.command(aliases=available_commands["help"])
async def help(ctx, *args):
    log_function("help", ctx)
    await cmd.help.help(client, ctx, *args)

    
@client.command(aliases=available_commands["clear"])
async def clear(ctx):
    if server := (await function_check(ctx, "clear")) is None: return
    await cmd.clear.clear(ctx, server.queue)


@client.command(aliases=available_commands["credits"])
async def credits(ctx):
    log_function("credits", ctx)
    await cmd.credits.credits(ctx)


@client.command(aliases=available_commands["forceskip"])
async def forceskip(ctx):
    if server := (await function_check(ctx, "forceskip")) is None: return
    await cmd.forceskip.force_skip(client, ctx, server.queue, server.bot_info)
    
   
@client.command(aliases=available_commands["join"])
async def join(ctx):
    if (await function_check(ctx, "join", False)) is None: return
    await cmd.join.join(ctx)

    
@client.command(aliases=available_commands["leave"])
async def leave(ctx):
    if await function_check(ctx, "leave") is None: return
    await cmd.leave.leave(ctx)


@client.command(aliases=available_commands["loop"])
async def loop(ctx):
    if server := (await function_check(ctx, "loop")) is None: return
    await cmd.loop.loop(ctx, server.bot_info)


@client.command(aliases=available_commands["loopqueue"])
async def loopqueue(ctx):
    if server := await function_check(ctx, "loopqueue") is None: return
    await cmd.loopqueue.loopqueue(ctx, server.bot_info)


@client.command(aliases=available_commands["lyrics"])
async def lyrics(ctx, *args):
    if server := (await function_check(ctx, "lyrics")) is None: return
    await cmd.lyrics.lyrics(ctx, server.queue, *args)


@client.command(aliases=available_commands["move"])
async def move(ctx, *args):
    if server := (await function_check(ctx, "move")) is None: return
    await cmd.move.move(ctx, server.queue, *args)


@client.command(aliases=available_commands["nowplaying"])
async def nowplaying(ctx):
    if server := (await function_check(ctx, "nowplaying")) is None: return
    await cmd.nowplaying.nowplaying(client, ctx, server.queue, server.counter)


@client.command(aliases=available_commands["pause"])
async def pause(ctx):
    if (await function_check(ctx, "pause")) is None: return
    await cmd.pause.pause(client, ctx)


@client.command(aliases=available_commands["play"])
async def play(ctx, *url):
    if server := (await function_check_play(ctx, "play")) is None: return
    await cmd.play.play(client, ctx, server.queue, server.bot_info, server.counter, *url)


@client.command(aliases=available_commands["playnow"])
async def playnow(ctx, *url):
    if server := (await function_check_play(ctx, "playnow")) is None: return
    await cmd.playnow.play_now(client, ctx, server.queue, server.bot_info, server.counter, *url)


@client.command(aliases=available_commands["playskip"])
async def playskip(ctx, *url):
    if server := (await function_check_play(ctx, "playskip")) is None: return
    await cmd.playskip.play_skip(client, ctx, server.queue, server.bot_info, server.counter,*url)


@client.command(aliases=available_commands["queue"])
async def queue_(ctx):
    if server := (await function_check(ctx, "queue")) is None: return
    await cmd.queue.queue(client, ctx, server.queue, server.bot_info, server.counter)


@client.command(aliases=available_commands["remove"])
async def remove(ctx, *args):
    if server := (await function_check(ctx, "remove")) is None: return
    await cmd.remove.remove(ctx, server.queue, *args)


@client.command(aliases=available_commands["resume"])
async def resume(ctx):
    if (await function_check(ctx, "resume")) is None: return
    await cmd.resume.resume(client, ctx)


@client.command(aliases=available_commands["search"])
async def search(ctx,*url):
    if server := (await function_check_play(ctx, "search")) is None: return
    await cmd.search.search(client, ctx, server.queue, server.bot_info, server.counter, *url)


@client.command(aliases=available_commands["seek"])
async def seek(ctx, *args):
    if server := (await function_check(ctx, "seek")) is None: return
    await cmd.seek.seek(client, ctx, server.queue, server.bot_info, *args)


@client.command(aliases=available_commands["shuffle"])
async def shuffle(ctx):
    if server := (await function_check(ctx, "shuffle")) is None: return
    await cmd.shuffle.shuffle(ctx, server.queue)