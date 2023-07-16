import logging

from discord.ext.commands import Context


logging.basicConfig(
        level=logging.INFO, 
        datefmt="%d-%m-%y %H:%M:%S",
        format="\n[%(asctime)s] %(module)s at %(lineno)s\n[%(levelname)s] %(message)s", 
)

log = logging.getLogger()


def log_command(ctx: Context, cmd: str):
    log.info(
        f"User '{ctx.author.name}' issued command '{cmd}' in channel {ctx.channel.name} ({ctx.guild.name})"
    )
