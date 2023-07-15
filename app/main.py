import discord
import os
from discord.ext.commands import Context, Bot
from dotenv import load_dotenv

from logger import logger
from commands import commands


load_dotenv()

command_prefix = "!"
instance = Bot(
            command_prefix=command_prefix,
            case_insensitive=True,
            help_command=None,
            intents=discord.Intents.all(),
        )

@instance.command(aliases=commands.get_all_aliases())
async def function_handler(ctx: Context, *args):
    # ignore command_prefix
    command = ctx.message.content.split(command_prefix)[1]
    commands.execute_command(command, ctx, *args)


@instance.event
async def on_ready():
    logger.info("Bot started successfully")
    await instance.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="!help")
    )



if __name__ == "__main__":
    instance.run(os.environ["DISCORD_TOKEN_DEV"])

