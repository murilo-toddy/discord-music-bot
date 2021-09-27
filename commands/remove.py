async def remove(ctx, queue, *args):
    if len(args) == 0:
        await ctx.channel.send("Você precisa especificar uma posição.")

    elif len(args) == 1:
        try:
            pos = int(*args[0])
        except:
            await ctx.channel.send("O argumento precisa ser um número válido!")
            return

        if pos > (len(queue)+1) and pos !=0:
            await ctx.channel.send("Índice inválido.\nPara ver os items da fila utilize ```!queue```")
            return

        url = queue.remove(pos)
        
        #TODO deixar mensagem bonita
        await ctx.channel.send("Item " + str(url) + " removido com sucesso.") 
    
    else:
        await ctx.channel.send("Sintaxe incorreta.")

