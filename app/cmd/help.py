from discord.ext.commands import Context 

from data.worker import Worker


async def help_function(worker: Worker, ctx: Context, *args):
    commands_dict = worker.commands.alias_to_command
    if not args or len(args) > 1 or args[0].lower() in commands_dict["help"].aliases:
        available_commands = worker.commands.get_all_commands()
        commands_per_line = 4
        available_commands_formatted = " ".join([
            f"`{cmd}`,\n" if (i + 1) % commands_per_line == 0 else f"`{cmd}`, " \
            for i, cmd in enumerate(available_commands)
        ])

        description = (
            f"_Use_ `!help <cmd>` _to get help for a\nspecific command_\n\n"
            f"**Available Commands:**\n"
            # escape last comma
            f"{available_commands_formatted[:-2]}\n"
        )
        await worker.send_embed_message(ctx, "**Help Command**", description)
        return

    cmd = args[0].lower()
    if cmd in worker.commands.get_all_aliases():
        command = worker.commands.alias_to_command[cmd]
        await worker.send_embed_message(
                ctx, 
                f"Help for: {command.name}", 
                (
                    f"**Aliases:** `{'`, `'.join(command.aliases)}`\n\n"
                    f"{command.description}"
                )
            )
        return

    title = "**Command not found**"
    desc = (
        f"_Unable to find command_ `{cmd}`\n"
        "_Use_ `!help` _to get a list of available commands_"
    )
    await worker.send_embed_message(ctx, title, desc)

