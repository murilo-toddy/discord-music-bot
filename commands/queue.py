import discord, asyncio,math
from utils import embedded_message, format_time

async def queue(client, ctx, queue, bot_info, counter):
    
    # Empty queue
    if len(queue) <= 1:
        await embedded_message(ctx, "**Empty Queue**", "_The queue is currently empty_")
        return

    loop = bot_info.get_loop()
    loop_queue = bot_info.get_loop_queue()

    pages = []
    description = ""
    num_pages = math.ceil((len(queue) - 1) / 10)
    total_time = await get_full_music_time(queue, counter)
    
    # i = 0
    for i in range(len(queue)):
        
        if i == 0:
            description += "\nCurrently playing"
            description += f" - [{queue[i]['title']}]({queue[i]['url']})"
            description += f" `{queue[i]['duration']}` ({queue[i]['user']})\n\n"
            i += 1
            continue

        else:
            description += f"{i}"
            description += f" - [{queue[i]['title']}]({queue[i]['url']})"
            description += f" `{queue[i]['duration']}` ({queue[i]['user']})\n"

        # Finished loading a page
        if i % 10 == 0 or i == (len(queue) - 1):
   
            if loop:
                description += "\n :repeat_one: **Loop** _enabled_"
            if loop_queue:
                description += "\n :repeat: **Loop Queue** _enabled_"

            if loop or loop_queue:
                description += "\n"

            description += f"\n Time until complete `{total_time}"
            description += f"`\n`{math.ceil(i/10)}/{num_pages}`"
            
            page = discord.Embed(
                title = f"**Queue Songs!  Total: `{len(queue)-1}` **",
                description = description,
                color = discord.Color.red()
            )

            description = ""
            
            page.set_footer(text = " Resquested by " + ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
            page.set_thumbnail(url = queue[0]["thumb"])
            pages.append(page)
            
            await asyncio.sleep(0.05)

        # i += 1
    
    await print_pages(client, ctx, pages)


async def print_pages(client, ctx, pages):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]  # skip to start, left, right, skip to end
    current = 0
    client.help_pages = pages
    msg = await ctx.send(embed=client.help_pages[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            embeded = client.help_pages[current]
            await msg.clear_reactions()

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if user != client.user:
                    if current > 0:
                        current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if user != client.user:
                    if current < len(client.help_pages)-1:
                        current += 1

            elif reaction.emoji == u"\u23E9":
                if user != client.user:
                    current = len(client.help_pages)-1

            for button in buttons:
                if user != client.user:
                    await msg.remove_reaction(button, user)

            if current != previous_page:
                await msg.edit(embed=client.help_pages[current])
                

async def get_full_music_time(queue, counter):
    total_time = sum(song["duration_seconds"] for song in queue)
    return format_time(total_time - await counter.get_time())
    