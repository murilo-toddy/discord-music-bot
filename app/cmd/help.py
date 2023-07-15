import logging 
from command_handler import Command


def help_function(*_):
    logging.info("help function called")


command = Command(
   func=help_function, 
   aliases=["help"], 
   description="""help"""
)

