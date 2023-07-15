import logging 
from command_handler import Command
import commands


def help_function(*_):
    print(commands)
    logging.info("help function called")


command = Command(
   func=help_function, 
   aliases=["help"], 
   description="""help"""
)

