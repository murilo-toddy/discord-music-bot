import aiohttp
from utils import embedded_message

async def lyrics(ctx, queue,*music_name):

    url_busca = "https://some-random-api.ml/lyrics?title="

    if len(music_name) != 0:
        url_busca += " ".join(music_name)
    
    elif len(queue) == 0:
        await embedded_message(ctx, "Not Playing", "No song currently playing")
        return

    else:
        url_busca += queue[0]["title"]
    
    async with aiohttp.request("GET", url_busca, headers={}) as response:
        if not 200 <= response.status <= 299:
            await embedded_message(ctx, "**Error in Lyrics**", "_We couldn't find_\n_the song lyrics_")
            return

        data = await response.json()

    await embedded_message(ctx, "**Lyrics - " + data["title"] + "**", data["lyrics"])