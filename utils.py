import discord

async def embedded_message(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        color = discord.Color.red()
    )

    embed.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embed)

