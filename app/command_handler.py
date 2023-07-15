import logging
from functools import reduce
import logging
from operator import iconcat
from typing import Callable


class Command:
    def __init__(self, func: Callable, aliases: list[str], description: str):
        self.func = func
        self.aliases = aliases
        self.description = description
        logging.info(f"Registered {aliases} with description {description}")


class Commands:
    def __init__(self, command_list: list[Command]):
        self.command_list = command_list
        self.command_dict = self.__create_command_dict(command_list)

    def __create_command_dict(self, command_list: list[Command]) -> dict[str, Callable]:
        command_dict = {}
        for command in command_list:
            for alias in command.aliases:
                command_dict[alias] = command.func
        return command_dict

    def get_all_aliases(self) -> str:
        return reduce(iconcat, [command.aliases for command in self.command_list], [])

    def execute_command(self, alias: str, *args):
        self.command_dict[alias](*args)

