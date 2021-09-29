import discord, asyncio
import commands as cmd

from config import *
from utils import *

from data_structure import Queue
from commands.log import log_function

# TODO
# - Criar classe mestre
# - Refatorar play
# - Refatorar buscas
# - Buscar playlist inteira de uma vez spotify
# - Implementar async


@client.event
async def on_ready():
    print("\n [!] Bot started.")
    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print("\n [!] Bot Status updated successfully.")
    
    asyncio.get_event_loop().create_task(counter.start_timer())
    for guild in client.guilds: 
        queue[str(guild.id)] = Queue()

    print("\n [!] Finished startup process")


@client.event
async def on_guild_join(guild):
    print("\n [!] Bot added to channel " + str(guild.name))
    queue[str(guild.id)] = Queue()



@client.command(aliases=["j"])
async def join(ctx):
    log_function("join")
    if not await verify_channel(ctx, False): return
    await cmd.join.join(ctx)


@client.command(aliases=["np"])
async def nowplaying(ctx):
    log_function("nowplaying")
    if not await verify_channel(ctx): return
    await cmd.nowplaying.nowplaying(client, ctx, queue[str(ctx.guild.id)])


@client.command(aliases=["loopq", "lq","loop queue"])
async def loopqueue(ctx):
    log_function("loopqueue")
    if not await verify_channel(ctx): return
    await cmd.loopqueue.loopqueue(ctx)


@client.command(aliases=["l"])
async def loop(ctx):
    log_function("loop")
    if not await verify_channel(ctx): return
    await cmd.loop.loop(ctx)


@client.command(aliases=["dc","disconnect"])
async def leave(ctx):
    log_function("leave")
    if not await verify_channel(ctx): return
    await cmd.leave.leave(ctx, queue[str(ctx.guild.id)])


@client.command(brief="", aliases=["p"])
async def play(ctx, *url):
    log_function("play")
    if not await verify_channel_play(ctx): return
    await cmd.play.play(client, ctx, queue[str(ctx.guild.id)], *url)


@client.command()
async def pause(ctx):
    log_function("pause")
    if not await verify_channel(ctx): return
    await cmd.pause.pause(client, ctx)


@client.command()
async def resume(ctx):
    log_function("resume")
    if not await verify_channel(ctx): return
    await cmd.resume.resume(client, ctx)


@client.command()
async def shuffle(ctx):
    log_function("shuffle")
    if not await verify_channel(ctx): return
    await cmd.shuffle.shuffle(ctx, queue[str(ctx.guild.id)])


@client.command(aliases=["m"])
async def move(ctx, *args):
    log_function("move")
    if not await verify_channel(ctx): return
    await cmd.move.move(ctx, queue[str(ctx.guild.id)], *args)


@client.command(aliases=["queue", "q"])
async def queue_(ctx):
    log_function("queue")
    if not await verify_channel(ctx): return
    await cmd.queue.queue(ctx, queue[str(ctx.guild.id)], client)


@client.command(aliases=["r"])
async def remove(ctx, *args):
    log_function("remove")
    if not await verify_channel(ctx): return
    await cmd.remove.remove(ctx, queue[str(ctx.guild.id)], *args)


@client.command(aliases=["fs", "skip", "s", "skp"])
async def forceskip(ctx):
    log_function("forceskip")
    if not await verify_channel(ctx): return
    await cmd.forceskip.force_skip(client, ctx)


@client.command(aliases=["c","clean"])
async def clear(ctx):
    log_function("clear")
    if not await verify_channel(ctx): return
    await cmd.clear.clear(ctx, queue[str(ctx.guild.id)])


@client.command()
async def seek(ctx, *args):
    log_function("seek")
    if not await verify_channel(ctx): return
    await cmd.seek.seek(client, ctx, queue[str(ctx.guild.id)], *args)
    

@client.command()
async def help(ctx, *args):
    log_function("help")
    await cmd.help.help(client, ctx, *args)



if __name__ == '__main__':
    client.run(TOKEN)



