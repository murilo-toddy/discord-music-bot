from utils import embedded_message

# Changes a song position in queue
async def move(ctx, queue, *args):
    if len(args) == 0:
        await embedded_message(ctx, ":japanese_goblin: **Invalid Syntax**", "_You must specify a position_")
    
    elif len(args) == 1:
        await move_to(ctx, queue, args[0], 1)

    elif len(args) == 2:
        await move_to(ctx, queue, args[0], args[1])

    else:
        await embedded_message(ctx, ":japanese_goblin: **Invalid Syntax**", "_Function only takes two arguments_")


async def move_to(ctx, queue, pos1, pos2):
    try:
        pos1 = int(pos1)
        pos2 = int(pos2)
    
    except:
        await embedded_message(ctx, ":japanese_goblin: **Invalid Syntax**", "_Argument must be a valid number_")
        print(" [!!] Error in \'move\' function\n      * Could not convert position!")
        return

    if pos1 >= len(queue) or pos2 > len(queue) or pos1 == 0 or pos2 == 0:
        await embedded_message(ctx, ":japanese_goblin: **Invalid Position**", "_To check the queue use_ `!queue`")
        return

    if pos1 == pos2:
        await embedded_message(ctx, ":japanese_goblin: **Invalid Position**", "_Song is already in position_ `" + str(pos1) + "`")
        return

    title = queue[pos1]["title"]
    queue.move(pos1, pos2)

    await embedded_message(ctx, title, "Changed `"+str(title)+"` position from `"+str(pos1)+"` to `"+str(pos2)+"`")

