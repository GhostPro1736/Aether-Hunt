from core import GameState, user
import random
class rolls:
    def __init__(self):
        self.tentativas = 100
    def roullete(self):
        self.rolls = input(f"Deseja fazer reroll? Você tem {self.tentativas} tentativas restantes. S para Sim ou N para Não: ")
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
            print(f"Sua aura atual é {aura_atual[0]}, ")
        else:
            print("Nossa que sorte! sua aura é perspicaz, é um tipo bem raro\nele libera habilidades únicas que outras auras não possuem")
        print(reroll.roullete())
    user.aura = aura_atual[0]