from core import user, GameState
from core.Ability import debug_choose_ability
from inputs import get_inputs
user.aura = "Perspicaz"
user.name = "GhostPro"
GameState.inicial = True
GameState.isAdmin = True
debug_choose_ability()
while not GameState.exit:
    get_inputs()