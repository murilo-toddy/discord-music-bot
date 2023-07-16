import logging
from functools import reduce
import logging
from operator import iconcat
from typing import Callable


class Command:
    def __init__(
            self, 
            name: str, 
            func: Callable, 
            aliases: list[str], 
            description: str,
        ):
        self.name = name
        self.func = func
        self.aliases = aliases
        self.description = description
        logging.info(f"Registered {aliases} with description {description}")


class Commands:
    def __init__(self, command_list: list[Command]):
        self.command_list = command_list
        self.alias_to_command= self.__create_alias_to_command_dict(command_list)
        self.name_to_command = self.__create_name_to_command_dict(command_list)

    def __create_alias_to_command_dict(self, command_list: list[Command]) -> dict[str, Command]:
        alias_to_command = {}
        for command in command_list:
            for alias in command.aliases:
                alias_to_command[alias] = command
        return alias_to_command 

    def __create_name_to_command_dict(self, command_list: list[Command]) -> dict[str, Command]:
        name_to_command = {}
        for command in command_list:
            name_to_command[command.name] = command
        return name_to_command

    def get_all_aliases(self) -> str:
        return reduce(iconcat, [command.aliases for command in self.command_list], [])

    def get_all_commands(self) -> list[str]:
        return [command.name for command in self.command_list]

    def get_command_from_alias(self, alias: str) -> Command:
        return self.alias_to_command[alias]

    def get_command_from_name(self, name: str) -> Command:
        return self.name_to_command[name]
    
    async def execute_command(self, alias: str, *args):
        await self.alias_to_command[alias].func(*args)

