import discord
from discord.ext.commands import Context

from command_handler import Commands
from data.server import Server


class Worker:
    def __init__(self, commands: Commands):
        self.commands = commands
        self.servers = {}

    def load(self, guilds):
        for guild in guilds:
            self.__create_server(guild)

    def __create_server(self, guild):
        self.servers[f"{guild.id}"] = Server()

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

