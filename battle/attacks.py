from typing import Optional, List
class Effect:
    def __init__(self, name: str, effect_type: str, buff_type: Optional[str]=None, stackable: bool=False, target: str="self", priority: int=1, max_duration: Optional[int]=None):
        self.name = name
        self.effect_type = effect_type
        self.buff_type = buff_type or []
        self.stackable = stackable
        self.target = target
        self.priority = priority
        self.max_duration = max_duration
    def atributes(self,duration: int =1, value: int=0, damage: int=0, trigger_condition: Optional[str]=None):
        self.duration = duration
        self.trigget_condition = trigger_condition
        self.damage = damage
        self.value = value
class Attacks:
    def __init__(self, isDef: bool =False, damage: int =0, type: str ="Normal", defense: int=0, hasEffect: bool = False, name: str ="", counter: int=0, counter_attack: int=0, counts: int =1, effects: Optional[List[Effect]]=None, min_level: int=1):
        self.type = type
        self.name = name
        self.min_level = min_level
        self.effects = effects or [] if hasEffect else []
        if not isDef:
            self.counter_attack = counter_attack
            self.damage = damage
            self.counts = counts
        else:
            self.defense = defense
            self.counter = counter