import commands as cmd
from config import *
from commands.log import log_function
from discord_slash.utils.manage_commands import create_choice, create_option

@slash.slash(
name="help",
    description="Shows help for specific commands",
    options=[
        create_option(
            name="command",
            description="Select a command",
            required=False,
            option_type=3,
            # choices=[
            #     create_choice(name="clear", value="clear"),
            #     create_choice(name="play", value="play")
            # ]
        )
    ]
)
async def _help(ctx: SlashContext, command="help"):
    log_function("help", ctx)
    await ctx.send(embeds=[cmd.help.get_embed(client, command)])