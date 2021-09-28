from utils import embedded_message

async def verify_channel(ctx, sender_equals_bot: bool = True):
    sender = ctx.author.voice
    if not sender:
        await embedded_message(ctx, "**Not Connected**", ":exclamation: _You must be connected to a voice channel_")
        return False

    sender_channel = sender.channel
    if sender_equals_bot:
        if ctx.guild.voice_client:
            bot_channel = ctx.guild.voice_client.channel
            if bot_channel != sender_channel:
                await embedded_message(ctx, "**Foreign detected :ghost:**", "_You must be in the same channel\n_" + 
                                                                            "_as the bot to issue this command_")
                return False
        else:
            await embedded_message(ctx, "**Not Connected**", ":exclamation: _I'm currently not connected_")
            return False
    return True


async def verify_channel_play(ctx):
    Sender = ctx.author.voice
    if not Sender:
        await embedded_message(ctx, "**Not Connected**", ":exclamation: _You must be connected to a voice channel_")  
        return False

    sender_channel = Sender.channel
    bot_channel = ctx.guild.voice_client
    if bot_channel:
        if not bot_channel.channel == sender_channel:
            await embedded_message(ctx, "**Foreign detected :ghost:**", "_You must be in the same channel\n_" + 
                                                                        "_as the bot to issue this command_")
            return False
        
        else:
            return True

    await ctx.author.voice.channel.connect()
    await embedded_message(ctx, "**:wave: Hello Hello**", "_Connected successfully_")
    bot_channel = ctx.guild.voice_client
    bot_channel.pause()
    return True