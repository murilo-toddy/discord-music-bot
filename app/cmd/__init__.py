from command_handler import Command, Commands
import cmd.help


commands = Commands([
    Command(
        name="help",
        func=cmd.help.help_function, 
        aliases=["help"], 
        description=""
    ),
    Command(
        name="clear",
        func=cmd.help.help_function, 
        aliases=["clear", "c", "clean"], 
        description=(
            "`!clear`\n"
            "Removes all songs from the queue"
        )
    ),
    Command(
        name="credits",
        func=cmd.help.help_function, 
        aliases=["credits", "creditos", "autores"], 
        description=(
            "`!credits`\n"
            "Shows information about authors"
        )
    ),
    Command(
        name="forceskip",
        func=cmd.help.help_function, 
        aliases=["forceskip", "fs", "skip", "s", "skp", "next"], 
        description=(
            "`!forceskip`\n"
            "Skips currently playing song"
        )
    ),
    Command(
        name="join",
        func=cmd.help.help_function, 
        aliases=["join", "j"], 
        description=(
            "`!join`\n"
            "Connects the bot to user's current voice channel"
        )
    ),
    Command(
        name="leave",
        func=cmd.help.help_function, 
        aliases=["leave", "dc", "disconnect"], 
        description=(
            "`!leave`\n"
            "Disconnects the bot from\n"
            "currently connected channel"
        )
    ),
    Command(
        name="loop",
        func=cmd.help.help_function, 
        aliases=["loop", "l"], 
        description=(
            "`!loop`\n"
            "Puts currently playing song in loop\n"
            "Song will repeat until skipped or loop is turned off"
        )
    ),
    Command(
        name="loopqueue",
        func=cmd.help.help_function, 
        aliases=["loopqueue", "loopq", "lq"], 
        description=(
            "`!loopqueue`\n"
            "Puts queue in loop\n"
            "Queue will repeat once all songs have eneded"
        )
    ),
    Command(
        name="lyrics",
        func=cmd.help.help_function, 
        aliases=["lyrics", "ly"], 
        description=(
            "`!lyrics`\n"
            "Shows the lyrics for currently playing song\n\n"
            "`!lyrics <query>`\n"
            "Shows the lyrics for searched song"
        )
    ),
    Command(
        name="move",
        func=cmd.help.help_function, 
        aliases=["move", "m", "mv"], 
        description=(
            "`!move <pos>`\n"
            "Moves song from `pos` to the top of the queue\n\n"
            "`!move <pos1> <pos2>`\n"
            "Moves song from `pos1` to `pos2`"
        )
    ),
    Command(
        name="nowplaying",
        func=cmd.help.help_function, 
        aliases=["nowplaying", "np"], 
        description=(
            "`!nowplaying`\n"
            "Shows information about currently playing song"
        )
    ),
    Command(
        name="pause",
        func=cmd.help.help_function, 
        aliases=["pause"], 
        description=(
            "`!pause`\n"
            "Pauses currently playing song"
        )
    ),
    Command(
        name="play",
        func=cmd.help.help_function, 
        aliases=["play", "p"], 
        description=(
            "`!play <query>`\n"
            "Enqueues song based on provided `query`\n"
            "Accepts _google search_, _youtube url_ or _spotify url_"
        )
    ),
    Command(
        name="playnext",
        func=cmd.help.help_function, 
        aliases=["playnext", "pn"], 
        description=(
            "`!playnow <query>`\n"
            "Inserts a new song based on `query` on top of the queue\n"
            "Accepts _google search_, _youtube url_ or _spotify url_"
        )
    ),
    Command(
        name="playskip",
        func=cmd.help.help_function, 
        aliases=["playskip", "ps"], 
        description=(
            "`!playnow <query>`\n"
            "Skip currently playing song and plays the one from `query` immediatly\n"
            "Accepts _google search_, _youtube url_ or _spotify url_"
        )
    ),
    Command(
        name="queue",
        func=cmd.help.help_function, 
        aliases=["queue", "q"], 
        description=(
            "`!queue`\n"
            "Lists all enqueued songs"
        )
    ),
    Command(
        name="remove",
        func=cmd.help.help_function, 
        aliases=["remove", "r"], 
        description=(
            "`!remove <pos>`\n"
            "Removes song from specified position from the queue"
        )
    ),
    Command(
        name="resume",
        func=cmd.help.help_function, 
        aliases=["resume", "continue"], 
        description=(
            "`!resume`\n"
            "Resumes song if paused"
        )
    ),
    Command(
        name="search",
        func=cmd.help.help_function, 
        aliases=["search", "se", "busca", "choose"], 
        description=(
            "`!search <query>`\n"
            "Shows first 5 results from youtube search based on `<query`\n"
            "to the user. A song can be selected by reacting to the bot's message"
        )
    ),
    Command(
        name="seek",
        func=cmd.help.help_function, 
        aliases=["seek"],
        description=(
            "`!seek <time>`\n"
            "Moves currently playing song to specified `time`"
            "Can be a number in `seconds` or `hh:mm:ss` format"
        )
    ),
    Command(
        name="shuffle",
        func=cmd.help.help_function, 
        aliases=["shuffle"],
        description=(
            "`!shuffle`\n"
            "Perfoms a random shuffle on the queue"
        )
    ),
])
