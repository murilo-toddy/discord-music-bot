from .play import FFMPEG_OPTIONS, play_next

async def seek(client, ctx, queue, *args):
    val = args[0]
    FFMPEG_OPTIONS["before_options"] = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -ss ' + str(val)
    await play_next(client, ctx, queue, seek=True)