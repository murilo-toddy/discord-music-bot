import discord

async def help(client, ctx, *args):

    title, description = get_description(*args)

    embed = discord.Embed(
        title = '',
        description = description,
        color = discord.Color.red()
    )

    embed.set_author(name=title,icon_url=client.user.avatar_url)
    await ctx.channel.send(embed=embed)



def get_description(*args):
    
    if not args or len(args) > 1 or args[0].lower() == "help":

        description = "_Use _`!help <command>` _to get help_\n_for a specific command_\n\n"
        
        description += "**Avaliable Commands:**\n"
        description += "`help`, `clear`, `credits`, `forceskip`, `join`,\n"
        description += "`leave`, `loop`, `loopqueue`, `lyrics`, `move`,\n"
        description += "`nowplaying`, `pause`, `play`, `playnow`, `playskip`,\n"
        description += "`queue`, `remove`, `resume`, `search`, `seek`,\n"
        description += "`shuffle`"

        return "Help Command", description

    else:
        arg = args[0]
        help_str = "Help command: "        
        clear = { "clear", "clean", "c" }
        if arg.lower() in clear:
            description = "_Aliases:_ `c`, `clean`"
            description += "\n\n**clear**\n"
            description += "Removes all songs from the queue"

            return help_str + "Clear", description

        credit = { "credits", "créditos", "creditos" }
        if arg.lower() in credit:
            description = "**credits**\n"
            description += "Shows information about authors"

            return help_str + "Credits", description

        forceskip = { "forceskip", "fs", "skip", "s", "skp"}
        if arg.lower() in forceskip:
            description = "_Aliases:_ `fs`, `skip`, `s`, `skp`"
            description += "\n\n**forceskip**\n"
            description += "Skips currently playing song"

            return help_str + "ForceSkip", description

        join = { "join", "j" }
        if arg.lower() in join:
            description = "_Aliases:_ `j`"
            description += "\n\n**join**\n"
            description += "Connects the bot to user's voice channel"

            return help_str + "Join", description

        leave = { "disconnect", "dc", "leave" }
        if arg.lower() in leave:
            description = "_Aliases:_ `disconnect`, `dc`"
            description += "\n\n**disconnect**\n"
            description += "Disconnects the bot from currently\nconnected voice channel"

            return help_str + "Disconnect", description
        
        loop = { "loop", "l" }
        if arg.lower() in loop:
            description = "_Aliases:_ `l`"
            description += "\n\n**loop**\n"
            description += "Puts currently playing song in loop\n"
            description += "Song will repeat until skipped or loop is turned off"

            return help_str + "Loop", description

        loopqueue = { "loopqueue", "loopq", "lq" }
        if arg.lower() in loopqueue:
            description = "_Aliases:_ `loopq`, `lq`"
            description += "\n\n*loopqueue*\n"
            description += "Puts queue in loop\n"
            description += "Queue will repeat when all songs\n"
            description += "have ended"

            return help_str + "LoopQueue", description

        loopqueue = { "lyrics", "ly" }
        if arg.lower() in loopqueue:
            description = "_Aliases:_ `ly`"
            description += "\n\n**lyrics**\n"
            description += "Shows the lyrics for\n"
            description += "currently playing song"
            description += "\n\n**lyrics** `query`\n"
            description += "Shows the lyrics for\n"
            description += "searched song"

            return help_str + "Lyrics", description

        move = { "move", "m", "mv" }
        if arg.lower() in move:
            description = "_Aliases:_ `m`, `mv`"
            description += "\n\n**move** `position`\n"
            description += "Moves song from `position` to\n"
            description += "the top of the queue"
            description += "\n\n**move** `from` `to`\n"
            description += "Moves song from position `from` to\n"
            description += "position `to`\n\n"
            description += "Arguments must be `positive integers`\n"
            description += "less than the length of the queue"

            return help_str + "Move", description

        np = { "nowplaying", "np" }
        if arg.lower() in np:
            description = "_Aliases:_ `np`"
            description += "\n\n**nowplaying**\n"
            description += "Reveals information about currently\n"
            description += "playing music"
        
            return help_str + "NowPlaying", description

        pause = { "pause" }
        if arg.lower() in pause:
            description = "**pause**\n"
            description += "Pauses currently playing song"
        
            return help_str + "Pause", description

        play = { "play", "p" }
        if arg.lower() in play:
            description = "_Aliases:_ `p`"
            description += "\n\n**play** `search_query`\n"
            description += "Plays song based on `search_query`"
            description += "\n\n**play** `youtube_url` or `spotify_url`\n"
            description += "Plays song or playlist from `url`"
            
            return help_str + "Play", description

        queue = { "queue", "q" }
        if arg.lower() in queue:
            description = "_Aliases:_ `q`"
            description += "\n\n**queue**\n"
            description += "Lists all enqueued songs"

            return help_str + "Queue", description

        remove = { "remove" }
        if arg.lower() in remove:
            description = "_Aliases:_ `r`"
            description += "\n\n**remove** `position`\n"
            description += "Removes song in `position` from\n"
            description += "the queue\n\n"
            description += "`position` must be a `positive integer`\n"
            description += "smaller than the length of the queue"

            return help_str + "Remove", description

        resume = { "resume" }
        if arg.lower() in resume:
            description = "**resume**\n"
            description += "Resumes paused song"

            return help_str + "Resume", description

        seek = { "seek" }
        if arg.lower() in seek:
            description = "**seek** `time`\n"
            description += "Moves currently playing song to\n"
            description += "specified time\n\n"
            description += "`time` must be in `hh:mm:ss` format or\n"
            description += "a time in `seconds` (`1:20` or `80`)"

            return help_str + "Seek", description

        shuffle = { "shuffle" }
        if arg.lower() in shuffle:
            description = "**shuffle**\n"
            description += "Performs a random shuffle in the queue"

            return help_str + "Shuffle", description

        search = { "search", "se", "srch", "busca", "choose" }
        if arg.lower() in search:
            description = "_Aliases:_ `se`, `srch`, `busca`, `choose`"
            description += "\n\n**search**\n"
            description += "Shows first 5 results from Youtube to the user\n"
            description += "A song can be selected by reacting to the bot's\n"
            description += "message"

            return help_str + "Search", description

        playnow = { "playnow", "pn" }
        if arg.lower() in playnow:
            description = "_Aliases:_ `pn`"
            description += "\n\n**playnow**\n"
            description += "Inserts a new song on the top of\n"
            description += "the queue or plays it if the queue\n"
            description += "is empty"

            return help_str + "Playnow", description

        playskip = { "playskip", "ps" }
        if arg.lower() in playskip:
            description = "_Aliases:_ `ps`"
            description += "\n\n**playskip**\n"
            description += "Inserts a new song on the top of\n"
            description += "the queue and skips currently playing\n"
            description += "if there's any"

            return help_str + "Playskip", description


        description = "_Command not Found_\nUse `!help` to see available commands"
        return "Command Not Found", description

