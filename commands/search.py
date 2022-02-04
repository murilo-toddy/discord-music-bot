import asyncio
import discord
import config
import googleapiclient.discovery
from utils import numbers_emoji, embedded_message
from search.search_utils import *
from .play import play_next, check_play_next
from .join import join

MUSICS_NUMBER = 5  # 1 to 10


async def search(client, ctx, queue, bot_info, counter, *args):
    global MUSICS_NUMBER

    if not args:
        await embedded_message(ctx, "Hey, nerd!", "You need to provide a search key")
        return

    search_query = " ".join(args)
    API_KEY = config.get_youtube_key()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

    search_response = youtube.search().list(
        q=search_query,
        part="id,snippet",
        type="video",
        maxResults=MUSICS_NUMBER,
        regionCode="BR"
    ).execute()

    search_vector = []
    for i in range(MUSICS_NUMBER):
        # search_info = {
        #     "id": search_response["items"][i]["id"]["videoId"],
        #     "url": "https://www.youtube.com/watch?v=" + search_info["id"],
        #     "title": search_response["items"][i]["snippet"]["title"]
        # }
        video_id = search_response["items"][i]["id"]["videoId"]
        search_vector.append({
            "id": video_id,
            "url": "https://www.youtube.com/watch?v=" + video_id,
            "title": search_response["items"][i]["snippet"]["title"]
        })

    choosen = await search_message(client, ctx, search_vector)

    if choosen == -1:
        return

    video_id = search_response["items"][choosen]["id"]["videoId"]

    response = youtube.videos().list(
        part='contentDetails,snippet',
        id=video_id,
        regionCode="BR",
    ).execute()

    set_video_info(ctx, response, queue)
    await show_message_video(response["items"][0]["snippet"]["title"], ctx, queue)
    await asyncio.sleep(0.1)

    if not ctx.guild.voice_client:
        await join(ctx, queue)
    loop = asyncio.get_event_loop()
    if check_play_next(client, ctx):
        loop.create_task(play_next(client, ctx, queue, bot_info, counter))
    return


async def search_message(client, ctx, search_vector):
    global MUSICS_NUMBER
    description = "\n"

    for i in range(MUSICS_NUMBER):
        description += f"{i + 1}"
        description += f" - [{search_vector[i]['title']}]({search_vector[i]['url']})\n\n"  # Com Link
        # description += " - "+str(search_vector[i]["title"]) + "\n\n" #Sem Link

    message_embed = discord.Embed(
        title="**Select your song!** :face_with_monocle: ",
        description=description,
        color=discord.Color.red()
    )

    message_embed.set_footer(text=" Resquested by " + ctx.message.author.name,
                             icon_url=ctx.message.author.avatar_url)

    msg = await ctx.send(embed=message_embed)

    for i in range(MUSICS_NUMBER):
        await msg.add_reaction(numbers_emoji[i])

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda r, u: u and r.emoji in numbers_emoji,
                                                   timeout=40.0)

        except asyncio.TimeoutError:
            await msg.clear_reactions()
            return -1

        else:
            for i in range(MUSICS_NUMBER):
                if reaction.emoji == numbers_emoji[i] and user != client.user:
                    return i
