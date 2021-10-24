import discord, commands.join as join

NumberToEmoji = []
NumberToEmoji.append ("1️⃣")
NumberToEmoji.append ("2️⃣")
NumberToEmoji.append ("3️⃣")
NumberToEmoji.append ("4️⃣")
NumberToEmoji.append ("5️⃣")
NumberToEmoji.append ("6️⃣")
NumberToEmoji.append ("7️⃣")
NumberToEmoji.append ("8️⃣")
NumberToEmoji.append ("9️⃣")
NumberToEmoji.append ("🔟")


async def returnNumberToEmoji():
    global NumberToEmoji
    return NumberToEmoji

async def embedded_message(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        color = discord.Color.red()
    )

    embed.set_footer(text= " Resquested by " + ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
    await ctx.channel.send(embed = embed)



def get_time_in_seconds(time):
    # Only seconds
    try:
        time = int(time)
        return time
    
    # hh:mm:ss format
    except:
        time_size = len(time)
        try:
            seconds = int(time[time_size-2:])
            if time_size == 4: minutes = int(time[time_size-4])
            else: minutes = int(time[time_size-5:time_size-3])
            time_in_secs = 60 * minutes + seconds
            
            # mm:ss format
            if time_size < 6:
                return time_in_secs
            
            # hh:mm:ss format
            if time_size == 7: hours = int(time[time_size-7])
            else: hours = int(time[time_size-8:time_size-6])
            return 60*60*hours + time_in_secs
        
        except:
            print(" [!!] Error in \'seek\'\n      * Could not convert number to seconds")
            return None



def format_time(time):
    seconds = format_subtime(str(time % 60))

    # Time is less than an hour
    if time < 3600:
        minutes = format_subtime(str(time // 60))
        return minutes + ":" + seconds

    # Time is more than an hour
    minutes = format_subtime(str(time // 60 % 60))
    hours = format_subtime(str(time // 3600))
    return hours + ":" + minutes + ":" + seconds


def format_subtime(subtime):
    if len(subtime) == 0: return "00"
    elif len(subtime) == 1: return "0" + subtime
    else: return subtime



async def verify_channel(ctx, sender_equals_bot: bool = True):
    sender = ctx.author.voice
    if not sender:
        await embedded_message(ctx, ":exclamation: **Not Connected**", "_You must be connected to a voice channel_")
        return False

    sender_channel = sender.channel
    if sender_equals_bot:
        if ctx.guild.voice_client:
            bot_channel = ctx.guild.voice_client.channel
            if bot_channel != sender_channel:
                await embedded_message(ctx, "**Foreign detected :ghost:**", "_You must be in the same channel_\n" + 
                                                                            "_as the bot to issue this command_")
                return False
        else:
            await embedded_message(ctx, ":exclamation: **Not Connected**", "_I'm currently not connected_")
            return False
    return True



async def verify_channel_play(ctx):
    sender = ctx.author.voice
    if not sender:
        await embedded_message(ctx, ":exclamation: **Not Connected**", "_You must be connected to a voice channel_")  
        return False

    sender_channel = sender.channel
    bot_channel = ctx.guild.voice_client
    if bot_channel:
        if bot_channel.channel == sender_channel:
            return True
    
        else:
            await embedded_message(ctx, "**Foreign detected :ghost:**", "_You must be in the same channel_\n" + 
                                                                        "_as the bot to issue this command_")
            return False
            
    await join.join_channel(ctx)
    return True


