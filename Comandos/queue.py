import sys
sys.path.append("..")
from EstruturaV2 import Lista

async def queue(ctx, queue: Lista):
    for item in queue:
        await ctx.channel.send(str(item))