from utils import embedded_message

async def credits(ctx):
    description = "_This bot was developed by_\n_Eduardo Valença and Murilo Todão_\n\n"
    description += "_Thank you for carying!_\n[GitHub Repository](https://github.com/murilo-toddy/discordbotpy)"
    await embedded_message(ctx, "**Credits** :moyai:", description)
    await add_reactions(ctx.message)
    

async def add_reactions(msg):
    await msg.add_reaction("🇵")
    await msg.add_reaction("🇮")
    await msg.add_reaction("🇳")
    await msg.add_reaction("🇹")
    await msg.add_reaction("🇴")
    await msg.add_reaction("🤠")
