from .gamestate import Gamestate
from .player import User, ability
from .Ability_options import Abilities
from rich.console import Console
console = Console()
GameState = Gamestate()
user = User()
def user_input(text, default=""):
    player_input = console.input(text)
    if player_input.strip() == "":
        return default
    else:
        return player_input