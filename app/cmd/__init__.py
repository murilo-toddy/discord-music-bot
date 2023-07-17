from command_handler import Command, Commands
import cmd.help


commands = Commands([
    Command(
        name="help",
        func=cmd.help.help_function, 
        aliases=["help"], 
        description="""help"""
    ),
    Command(
        name="play",
        func=cmd.help.help_function, 
        aliases=["play", "p"], 
        description="""play"""
    ),
])
