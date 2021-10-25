from utils import embedded_message

# Removes song from queue
async def remove(ctx, queue, *args):
    if len(args) == 0:
        await embedded_message(ctx, ":exclamation: **Invalid Syntax**", "You must specify a position")

    elif len(args) == 1:
        try:
            pos = int(args[0])
        except:
            await embedded_message(ctx, ":exclamation: **Invalid Syntax**", "Position has to be a valid number")
            return

        if pos > (len(queue)+1) and pos !=0:
            await embedded_message(ctx, ":exclamation: **Invalid Position**", "To check the queue, use `!queue`")
            return

        music = queue.remove(pos)
        await embedded_message(ctx, "**Removed**", f"`{music['title']}` _was successfully removed_")
    
    else:
        await embedded_message(ctx, ":exclamation: **Invalid Syntax**", "Function only takes two arguments")
