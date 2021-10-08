import aiohttp
from utils import embedded_message

async def lyrics(ctx, queue):

    if len(queue) == 0:
        await embedded_message(ctx, "Not Playing", "No song currently playing")
    
    async with aiohttp.request("GET", "https://some-random-api.ml/lyrics?title=" + queue[0]["title"], headers={}) as response:
        if not 200 <= response.status <= 299:
            await embedded_message(ctx, "**Error in Lyrics**", "_We couldn't find_\n_the song lyrics_")
            return

        data = await response.json()

    await embedded_message(ctx, "**Lyrics - " + data["title"] + "**", data["lyrics"])