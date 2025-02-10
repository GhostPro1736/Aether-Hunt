from core import GameState, user, console
from rich.prompt import Prompt
import random
class rolls:
    def __init__(self):
        self.tentativas = 100
    def roullete(self):
        self.rolls = Prompt.ask(f"Deseja fazer reroll? Você tem [b red]{self.tentativas}[/] tentativas restantes. [green][b]S[/b] para Sim[/green] ou [red][b]N[/b] para Não[/red]")
        if self.tentativas > 0:
            if self.rolls.lower() == "s":
                self.tentativas -= 1
                return "Girando... Agora: "
            elif self.rolls.lower() == "n":
                GameState.inicial = True
                return "cancelando..."
            else:
                GameState.inicial = True
                return "Desculpe não entendi, cancelando..."
        else:
            GameState.inicial = True
            return "Infelizmente, acabaram suas tentativas"
reroll = rolls()
def type_aura(): 
    while GameState.inicial == False:
        types_aura = ("Bastion", "Flux", "Morphic", "Forge", "Puppet", "Perspicaz")
        aura_atual = random.choices(types_aura, weights=[27,24,19,15,15,0.1], k=1)
        if aura_atual != "Perspicaz":
            console.print(f"Sua aura atual é [green]{aura_atual[0]}[/]")
        else:
            print("Nossa que sorte! sua aura é perspicaz, é um tipo bem raro\nele libera habilidades únicas que outras auras não possuem")
        print(reroll.roullete())
    user.aura = aura_atual[0]