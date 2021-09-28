import discord

async def help(client, ctx, *args):

    description = get_description(args)

    embed = discord.Embed(
        title = '',
        description = description,
        color = discord.Color.red()
    )

    embed.set_author(name='Help Command',icon_url=client.user.avatar_url)
    await ctx.channel.send(embed=embed)



def get_description(args):
    
    if len(args) == 0:

        description = "_Use _`!help <command>` _to get help_\n_for a specific command_\n\n"

        description += "**Avaliable Commands:**\n"
        description += "`help`, `clear`, `forceskip`, `join`, `leave`\n"
        description += "`loop`, `loopqueue`, `move`, `nowplaying`\n"
        description += "`pause`, `play`, `queue`, `remove`, `resume`\n"
        description += "`seek`, `shuffle`\n"

        return description


    else:

        description = "_Help for this command is not yet implemented_"
        return description
