import discord
from command import available_commands

command_descriptions = {
    "clear": "Removes all songs from the queue",
    "credits": "Shows information about authors",
    "forceskip": "Skips currently playing song",
    "join": "Connects the bot to user's voice channel",
    "leave": 
        "Disconnects the bot from currently\n" \
        "connected voice channel",
    "loop": 
        "Puts currently playing song in loop\n" \
        "Song will repeat until skipped or loop is turned off",
    "loopqueue":  
        "Puts queue in loop\n" \
        "Queue will repeat when all songs\n" \
        "have ended",
    "lyrics": 
        "Shows the lyrics for\n" \
        "currently playing song" \
        "\n\n**lyrics** `query`\n" \
        "Shows the lyrics for\n" \
        "searched song",
    "move": 
        "Moves song from first argument to\n" \
        "second argument. If second argument\n" \
        "is none, the song will be moved\n" \
        "to the top of the queue",
    "nowplaying": 
        "Shows information about currently\n" \
        "playing song",
    "pause": "Pauses currently playing song",
    "play": 
        "Enqueues song based on a search\n" \
        "query or provided youtube / spotify url",
    "playnow":             
        "Inserts a new song on the top of\n" \
        "the queue or plays it if the queue\n" \
        "is empty",
    "playskip": 
        "Inserts a new song on the top of\n" \
        "the queue and skips currently playing\n" \
        "if there's any",
    "queue": "Lists all enqueued songs",
    "remove": 
        "Removes song in specified position\n" \
        "from the queue",
    "resume": "Resumes paused song",
    "search": 
        "Shows first 5 results from Youtube to the user\n" \
        "A song can be selected by reacting to the bot's\n" \
        "message",
    "seek": 
        "Moves currently playing song to\n" \
        "specified time\n\n" \
        "argument must be in `hh:mm:ss` format or\n" \
        "a time in `seconds` (`1:20` or `80`)",
    "shuffle": "Performs a random shuffle in the queue"
}


async def help(client, ctx, *args): 
    await ctx.channel.send(embed=get_embed(client, *args))

def get_embed(client, *args):
    title, description = get_description(*args)
    embed = discord.Embed(title = '', description = description, color = discord.Color.red())
    embed.set_author(name=title,icon_url=client.user.avatar_url)
    return embed


def get_description(*args):

    commands = list(available_commands.keys())
    if not args or len(args) > 1 or args[0].lower() == "help":
        return "Help Command", get_default_desc(commands)

    arg = args[0].lower()
    help_str = "Help command: "

    for cmd in commands:
        if arg == cmd or arg in available_commands[cmd]:
            description = get_command_desc(cmd)
            description += command_descriptions[cmd]
            return help_str + cmd.capitalize(), description

    description = "_Command not Found_\nUse `!help` to see available commands"
    return "Command Not Found", description



def get_default_desc(commands):
    description = (
        "_Use _`!help <command>` _to get help_\n_for a specific command_\n\n" \
        "**Avaliable Commands:**\n" \
    )

    lines = 5
    inline_commands = (len(commands) // lines)
    
    for i in range(lines+1):
        description += ", ".join(f"`{cmd}`" for cmd in commands[i*inline_commands:(i+1)*inline_commands])
        if i != lines: description += ",\n"


def get_command_desc(cmd: str):
    desc = "_Aliases:_ "
    desc += ", ".join(f"`{alias}`" for alias in available_commands[cmd])
    desc += f"\n\n**{cmd}**\n"
    return desc
            
        
