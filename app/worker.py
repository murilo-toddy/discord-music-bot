from discord.ext.commands import Context
import discord

from command_handler import Commands


class Worker:
    def __init__(self, commands: Commands):
        self.commands = commands

    async def send_embed_message(
        self,
        ctx: Context,
        title: str,
        description: str,
    ):
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Color.random(),
        )
        embed.set_footer(
            text=" Resquested by " + ctx.message.author.name,
            icon_url=ctx.message.author.avatar
        )
        await ctx.channel.send(embed=embed)

