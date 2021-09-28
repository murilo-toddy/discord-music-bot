from utils import embedded_message

# Removes song from queue
async def remove(ctx, queue, *args):
    if len(args) == 0:
        await embedded_message(ctx, ":exclamation: **Invalid Syntax**", "_You must specify a position_")

    elif len(args) == 1:
        try:
            pos = int(*args[0])
        except:
            await embedded_message(ctx, ":exclamation: **Invalid Syntax**", "_Position has to be a valid number_")
            return

        if pos > (len(queue)+1) and pos !=0:
            await embedded_message(ctx, ":exclamation: **Invalid Position**", "_To check the queue use_ `!queue`")
            return

        music = queue.remove(pos)
        await embedded_message(ctx, "**Removed**", "`" + music["title"] + "` _was successfully removed_")
    
    else:
        await embedded_message(ctx, ":exclamation: **Invalid Syntax**", "_Function only takes two arguments_")

