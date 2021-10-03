import discord, asyncio,math
from utils import embedded_message, format_time

async def queue(client, ctx, queue, counter):
    
    # Empty queue
    if(len(queue)) <= 1:
        await embedded_message(ctx, "**Empty Queue**", "_The queue is currently empty_")
        return

    pages = []
    description = ""
    num_pages = math.ceil((len(queue) - 1) / 10)
    total_time = await get_full_music_time(queue, counter)
    
    for i in range(1, len(queue)):
        
        description += str(i) 
        description += " - ["+str(queue[i]["title"]) + "]("+str(queue[i]["url"]) + ")"
        description += " `" + str(queue[i]["duration"]) + "` ("+str(queue[i]["user"]) + ")\n"

        # Finished loading a page
        if i % 10 == 0 or i == (len(queue) - 1):
            
            description += "\n Time until complete `" + total_time
            description += "`\n`" + str(math.ceil(i/10)) + "/" + str(num_pages)+ "`"
            
            page = discord.Embed(
                title = "**Queue Songs!  Total: `"+str(len(queue)-1)+"` **",
                description = description,
                color = discord.Color.red()
            )

            description = ""

            page.set_footer(text = " Resquested by " + ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
            page.set_thumbnail(url = queue[0]["thumb"])
            pages.append(page)

        if i % 10 == 0:
            await asyncio.sleep(0.05)
    
    await print_pages(client, ctx, pages)


async def print_pages(client, ctx, pages):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
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
    total_time = 0
    for i in range(len(queue)):
        total_time += queue[i]["duration_seconds"]

    return format_time(total_time - await counter.get_time())
    