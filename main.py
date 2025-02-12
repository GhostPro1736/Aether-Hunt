from inicialização import title, name, type_aura
from core import GameState, user
from core.Ability import choose_ability
from inputs import get_inputs
if title():
    print("Ótimo, primeiro vamos ver seu nome")
    name()
else: 
    print("Desculpe não entendi, reinicie para continuar")
if user.name != None:
    type_aura()
if GameState.inicial:
    choose_ability()
    while not GameState.exit:
        get_inputs()