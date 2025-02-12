from typing import Optional, List
class Effect:
    def __init__(self, name: str, effect_type: str, buff_type: Optional[str]=None, stackable: bool=False, target: str="self", priority: int=1, max_duration: Optional[int]=None):
        self.name = name
        self.effect_type = effect_type
        self.buff_type = buff_type or ()
        self.stackable = stackable
        self.target = target
        self.priority = priority
        self.max_duration = max_duration
class Attacks:
    def __init__(self, isDef: bool =False, damage: int =0, type: str ="Normal", defense: int=0, name: str ="", effects: Optional[List[Effect]]=None, min_level: int=1):
        self.type = type
        self.name = name
        self.min_level = min_level
        self.effects_attr = {}
        self.effects = {}
        for effect in effects:
            try:
                self.effects[getattr(effect, "name")] = effect
            except NameError as e:
                print(f"O ataque não existe, erro {e}")
        if not isDef:
            self.damage = damage
        else:
            self.defense = defense
    def add_effect_attributes(self,effect_name: str="", effect_duration: int=1, effect_trigger: Optional[str]=None, buff_value: int=0, damage: int=0):
        if len(effect_name) < 1:
            raise NameError("Digite o nome do efeito desejado")
        elif not isinstance(effect_name, str):
            raise ValueError("O nome do efeito deve ser uma string")
        else:
            if effect_name not in self.effects:
                raise NameError("Efeito não encontrado no ataque principal")
            else:
                self.effects_attr[effect_name] = {"duration": effect_duration, "trigger": effect_trigger, "buff_value": buff_value, "damage": damage}
    def get_attributes(self, effect_name: str, attribute: str=""):
        if len(effect_name) < 1:
            raise NameError("Digite o nome do efeito desejado")
        elif not isinstance(effect_name, str):
            raise ValueError("O nome do efeito deve ser uma string")
        elif effect_name not in self.effects:
            raise NameError("O efeito não foi adicionado aos efeitos do ataque")
        else:
            if len(attribute) < 1:
                attribute = {}
                for attr, value in self.effects_attr[effect_name].items():
                    attribute[attr] = value
                return attribute
            elif not isinstance(attribute, str):
                raise ValueError("O nome do atributo desejado deve ser uma string")
            else:
                return self.effects_attr[effect_name][attribute]