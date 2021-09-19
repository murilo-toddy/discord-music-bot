from .play import ChangeLoop
import log

async def loop(client, ctx):
    log.log_function("loop")
    await ChangeLoop()