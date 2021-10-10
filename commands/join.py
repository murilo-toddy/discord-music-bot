import utils

# Connects the bot to a voice channel
async def join(ctx, queue, dc_counter):

    if ctx.guild.voice_client:
        await utils.embedded_message(ctx, "**Already Connected**", "_I am already connected to a voice channel_")
    
    else:
        await join_channel(ctx, queue, dc_counter)
        
        
async def join_channel(ctx, queue, dc_counter):
    queue.clear()
    await dc_counter.reset()

    await ctx.author.voice.channel.connect()
    ctx.guild.voice_client.stop()
    await utils.embedded_message(ctx, "**:wave: Hello Hello**", "_Connected successfully_")