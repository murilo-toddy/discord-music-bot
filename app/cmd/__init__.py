from command_handler import Command 
import cmd.help


help_command = Command(
    name="help",
    func=cmd.help.help_function, 
    aliases=["help"], 
    description="""help"""
)

play_command = Command(
    name="play",
    func=cmd.help.help_function, 
    aliases=["play", "p"], 
    description="""play"""
)

