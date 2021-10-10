import discord, asyncio, commands as cmd

from commands.log import log_function

from config import *
from utils import *


@client.event
async def on_ready():
    print("\n [!] Bot started.")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print("\n [!] Bot Status updated successfully.")
    bot.startup(client.guilds)
    periodic_refresh.start()
    print("\n [!] Finished startup process")


@client.event
async def on_guild_join(guild):
    print("\n [!] Bot added to server " + str(guild.name))
    bot.new_server(guild)


@client.event
async def on_voice_state_update(member, before, after):
    if member.id != client.user.id:
        return

    if after.channel == None:
        queue = bot.server[str(before.channel.guild.id)].queue
        queue.clear()

    if before.channel == None:     
        voice = after.channel.guild.voice_client
        time = 0
        while True:
            await asyncio.sleep(1)
            time = time + 1
            if voice.is_playing() or voice.is_paused():
                time = 0
            if time == 180:
                await voice.disconnect()
            if not voice.is_connected():
                break
    
    if before.channel != None and after.channel != None:
        counter = bot.server[str(after.channel.guild.id)].counter
        bot_info = bot.server[str(after.channel.guild.id)].bot_info

        bot_info.seek_set_true(await counter.get_time())
        discord.utils.get(client.voice_clients, guild=after.channel.guild).stop()


@tasks.loop(minutes=20)
async def periodic_refresh():
    print(" [!] Refreshing server variables")



@client.command()
async def help(ctx, *args):
    log_function("help")
    await cmd.help.help(client, ctx, *args)


@client.command(aliases=["creditos", "créditos", "autores"])
async def credits(ctx):
    log_function("credits")
    await cmd.credits.credits(ctx)


@client.command(aliases=["c","clean"])
async def clear(ctx):
    log_function("clear")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    await cmd.clear.clear(ctx, queue)


@client.command(aliases=["fs", "skip", "s", "skp"])
async def forceskip(ctx):
    log_function("forceskip")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    bot_info = bot.server[str(ctx.guild.id)].bot_info
    await cmd.forceskip.force_skip(client, ctx, queue, bot_info)

@client.command(aliases=["j"])
async def join(ctx):
    log_function("join")
    if not await verify_channel(ctx, False): return
    queue = bot.server[str(ctx.guild.id)].queue
    await cmd.join.join(ctx, queue)


@client.command(aliases=["dc","disconnect"])
async def leave(ctx):
    log_function("leave")
    if not await verify_channel(ctx): return 
    queue = bot.server[str(ctx.guild.id)].queue
    await cmd.leave.leave(ctx, queue)


@client.command(aliases=["l"])
async def loop(ctx):
    log_function("loop")
    if not await verify_channel(ctx): return
    bot_info = bot.server[str(ctx.guild.id)].bot_info
    await cmd.loop.loop(ctx, bot_info)


@client.command(aliases=["loopq", "lq"])
async def loopqueue(ctx):
    log_function("loopqueue")
    if not await verify_channel(ctx): return
    bot_info = bot.server[str(ctx.guild.id)].bot_info
    await cmd.loopqueue.loopqueue(ctx, bot_info)


@client.command(aliases=["ly"])
async def lyrics(ctx,*music_name):
    log_function("lyrics")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    await cmd.lyrics.lyrics(ctx, queue,*music_name)


@client.command(aliases=["m","mv"])
async def move(ctx, *args):
    log_function("move")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    await cmd.move.move(ctx, queue, *args)


@client.command(aliases=["np"])
async def nowplaying(ctx):
    log_function("nowplaying")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    counter = bot.server[str(ctx.guild.id)].counter
    await cmd.nowplaying.nowplaying(client, ctx, queue, counter)


@client.command()
async def pause(ctx):
    log_function("pause")
    if not await verify_channel(ctx): return
    await cmd.pause.pause(client, ctx)


@client.command(aliases=["p"])
async def play(ctx, *url):
    log_function("play")
    queue = bot.server[str(ctx.guild.id)].queue
    if not await verify_channel_play(ctx, queue): return
    bot_info = bot.server[str(ctx.guild.id)].bot_info
    counter = bot.server[str(ctx.guild.id)].counter
    await cmd.play.play(client, ctx, queue, bot_info, counter, *url)


@client.command(aliases=["queue", "q"])
async def queue_(ctx):
    log_function("queue")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    counter = bot.server[str(ctx.guild.id)].counter
    bot_info = bot.server[str(ctx.guild.id)].bot_info
    await cmd.queue.queue(client, ctx, queue,bot_info, counter)


@client.command(aliases=["r"])
async def remove(ctx, *args):
    log_function("remove")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    await cmd.remove.remove(ctx, queue, *args)


@client.command()
async def resume(ctx):
    log_function("resume")
    if not await verify_channel(ctx): return
    await cmd.resume.resume(client, ctx)


@client.command()
async def seek(ctx, *args):
    log_function("seek")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    bot_info = bot.server[str(ctx.guild.id)].bot_info
    await cmd.seek.seek(client, ctx, queue, bot_info, *args)


@client.command()
async def shuffle(ctx):
    log_function("shuffle")
    if not await verify_channel(ctx): return
    queue = bot.server[str(ctx.guild.id)].queue
    await cmd.shuffle.shuffle(ctx, queue)



if __name__ == '__main__':
    client.run(TOKEN)

