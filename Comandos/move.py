import sys
sys.path.append("..")

from EstruturaV2 import Lista

async def move(ctx, queue, *args):
    if len(args) == 0:
        await ctx.channel.send("precisa fornecer uma posicao")
    
    elif len(args) == 1:
        try:
            pos = int(*args[0])

        except:
            await ctx.channel.send("tem que inserir um numero valido")
            return

        if pos > len(queue):
            await ctx.channel.send("Posicao invalida arrombado")
            return

        queue.move((pos-1),0)
        await ctx.channel.send("movi de " + args[0] + " para 1")
            


    elif len(args) == 2:
        try:
            pos1 = int(*args[0])
            pos2 = int(*args[1])
            
            if pos1 > len(queue) or pos2 > len(queue):
                await ctx.channel.send("Posicao invalida arrombado")
                return

            await ctx.channel.send("mandei o " + args[0] + " pra " + args[1])

        except:
            await ctx.channel.send("vc nao mandou numero direito corno")

    else:
        await ctx.channel.send("sintaxe incorreta")