import aiohttp
from utils import embedded_message


async def lyrics(ctx, queue, *music_name):
    search_url = "https://some-random-api.ml/lyrics?title="
    if music_name: search_url += " ".join(music_name)
    
    elif len(queue) == 0:
        await embedded_message(ctx, "Not Playing", "No song currently playing")
        return

    else:
        search_url += queue[0]["title"]
    
    async with aiohttp.request("GET", search_url, headers={}) as response:
        if not 200 <= response.status <= 299:
            await embedded_message(ctx, "**Error in Lyrics**", "_We couldn't find_\n_the song lyrics_")
            return

        data = await response.json()

    await embedded_message(ctx, f"**Lyrics - {data['title']}**", data["lyrics"])
