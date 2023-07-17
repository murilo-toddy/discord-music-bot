import discord
from discord.ext.commands import Context, Bot

import logger
from auth import authentication
from data.worker import Worker
from cmd import commands



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
    logger.log_command(ctx, command, *args)
    await commands.execute_command(command, worker, ctx, *args)


@instance.event
async def on_ready():
    logger.log.info("Bot initialized")
    await instance.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="!help")
    )
    logger.log.info("Bot status updated successfully")


if __name__ == "__main__":
    instance.run(authentication["DISCORD_TOKEN_DEV"])

