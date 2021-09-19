import sys
sys.path.append("..")

from EstruturaV2 import Lista

async def shuffle(ctx, queue):
    queue.shuffle()