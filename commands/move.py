async def move(ctx, queue, *args):
    if len(args) == 0:
        await ctx.channel.send("precisa fornecer uma posicao :japanese_goblin:")
    
    elif len(args) == 1:
        try:
            pos = int(*args[0])

        except:
            await ctx.channel.send("tem que inserir um numero valido :japanese_goblin:")
            return

        if pos > (len(queue)+1) and pos !=0:
            await ctx.channel.send("Posicao invalida arrombado :japanese_goblin:")
            return

        queue.move((pos),1)
        await ctx.channel.send("movi de " + args[0] + " para 1")
            


    elif len(args) == 2:
        try:
            pos1 = int(*args[0])
            pos2 = int(*args[1])
            
            if pos1 > (len(queue)+1) or pos2 > (len(queue)+1) and pos1!=0 and pos2 !=0:
                await ctx.channel.send("Posicao invalida arrombado :japanese_goblin:")
                return

            queue.move((pos1),pos2)
            await ctx.channel.send("mandei o " + args[0] + " pra " + args[1])

        except:
            await ctx.channel.send("vc nao mandou numero direito corno :japanese_goblin:")

    else:
        await ctx.channel.send("sintaxe incorreta")