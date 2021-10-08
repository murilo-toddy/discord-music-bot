from utils import embedded_message

# Connects the bot to a voice channel
async def join(ctx, queue, dc_counter):

    queue.clear()
    await dc_counter.reset()

    if ctx.guild.voice_client:
        await embedded_message(ctx, "**Already Connected**", "_I am already connected to a voice channel_")
    
    else:
        await ctx.author.voice.channel.connect()
        ctx.guild.voice_client.pause()
        await embedded_message(ctx, "**:wave: Hello Hello**", "_Connected successfully_")
        