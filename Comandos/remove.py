async def remove(ctx, queue, *args):
    
    if len(args) == 0:
        await ctx.channel.send("é necessário fornecer uma posicao")

    elif len(args) == 1:
        try:
            pos = int(*args[0])
        except:
            await ctx.channel.send("insira um numero valido")
            return

        if pos > len(queue):
            await ctx.channel.send("out of bounds")
            return

        url = queue.remove(pos-1)
        await ctx.channel.send("item " + str(url) + " removido") 
    
    else:
        await ctx.channel.send("sintaxe incorreta")

