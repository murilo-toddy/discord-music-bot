from .play import ChangeLoopQueue
import log

async def loopqueue(client, ctx):
    log.log_function("loopqueue")
    await ChangeLoopQueue()