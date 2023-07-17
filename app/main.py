import discord
from discord.ext.commands import Context, Bot

from auth import authentication
from logger import log
from cmd import commands
from worker import Worker


command_prefix = "!"
instance = Bot(
        command_prefix=command_prefix,
        case_insensitive=True,
        help_command=None,
        intents=discord.Intents.all(),
    )

worker = Worker(commands)


@instance.command(aliases=commands.get_all_aliases())
async def function_handler(ctx: Context, *args):
    # ignore command_prefix
    command, *args = ctx.message.content.split(command_prefix)[1].split(" ")
    await commands.execute_command(command, worker, ctx, *args)


@instance.event
async def on_ready():
    log.info("Bot initialized")
    await instance.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="!help")
    )
    log.info("Bot status updated successfully")


if __name__ == "__main__":
    instance.run(authentication["DISCORD_TOKEN_DEV"])

