import logger
from discord.ext.commands import Context 

from worker import Worker


async def help_function(worker: Worker, ctx: Context, *args):
    logger.log_command(ctx, "help")

    commands_dict = worker.commands.alias_to_command
    if not args or len(args) > 1 or args[0].lower() in commands_dict["help"].aliases:
        await worker.send_embed_message(ctx, "ajuda", "desc")
        return

    cmd = args[0].lower()
    if cmd in worker.commands.get_all_aliases():
        print("command in list")
        await worker.send_embed_message(ctx, "command found", "desc")
        return

    title = "**Command not found**"
    desc = (
        f"_Unable to find command_ `{cmd}`\n"
        "_Use_ `!help` _to get a list of available commands_"
    )
    await worker.send_embed_message(ctx, title, desc)

