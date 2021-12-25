import asyncio, commands
from command import *
from config import *
from utils import *
from slash import *


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
    print(f"\n [!] Bot added to server {guild.name}")
    bot.new_server(guild)


@tasks.loop(minutes=20)
async def periodic_refresh():
    print(" [!] Refreshing server variables")


@client.event
async def on_voice_state_update(member, before, after):
    if member.id != client.user.id:
        return

    if after.channel is None:
        await bot.server[str(before.channel.guild.id)].reset()

    if before.channel is None:
        await bot.server[str(after.channel.guild.id)].reset()
        voice = after.channel.guild.voice_client
        time = 0
        while True:
            await asyncio.sleep(1)
            time += 1
            if voice.is_playing() or voice.is_paused():
                time = 0
            if time == 10:
                try:
                    await voice.disconnect()
                finally:
                    break

    if before.channel is not None and after.channel is not None:
        counter = bot.server[str(after.channel.guild.id)].counter
        bot_info = bot.server[str(after.channel.guild.id)].bot_info

        bot_info.seek_set_true(await counter.get_time())
        discord.utils.get(client.voice_clients, guild=after.channel.guild).stop()


if __name__ == '__main__':
    client.run(TOKEN)
