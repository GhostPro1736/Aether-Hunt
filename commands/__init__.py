import os
import importlib
def get_commands(commands_dir='commands'):
    commands = {}
    for commandname in os.listdir(commands_dir):
        if commandname.endswith('.py') and not commandname == "__init__.py":
            command_name = commandname[:-3]
            command = importlib.import_module(f"{commands_dir}.{command_name}")
            commands[command_name] = getattr(command, "execute", None)
    return commands