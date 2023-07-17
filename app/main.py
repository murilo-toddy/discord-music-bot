import discord
from discord.ext.commands import Context, Bot

import logger
from auth import authentication
from data.worker import Worker
from cmd import commands


COMMAND_PREFIX = "!"
instance = Bot(
        command_prefix=COMMAND_PREFIX,
        case_insensitive=True,
        help_command=None,
        intents=discord.Intents.all(),
    )

worker = Worker(commands)


@instance.command(aliases=commands.get_all_aliases())
async def function_handler(ctx: Context, *args):
    # ignore command_prefix
    command, *args = ctx.message.content.split(COMMAND_PREFIX)[1].split(" ")
    logger.log_command(ctx, command, *args)
    await commands.execute_command(command, worker, ctx, *args)


@instance.event
async def on_ready():
    logger.log.info("Bot initialized")
    await instance.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="!help")
    )
    logger.log.info("Bot status updated successfully")
    worker.load(instance.guilds)
    logger.log.info("Successfully created all servers")


if __name__ == "__main__":
    instance.run(authentication["DISCORD_TOKEN_DEV"])

