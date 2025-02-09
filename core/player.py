class User():
    def __init__(self):
        self.level = 1
        self.aura = None
        self.name = None
        self.exp = 0
        self.inventory = None
        self.status = Status()
        self.remainexp = 10
        self.ability = ability()
    def level_up(self):
        taxes = {range(1,11): 1.5, range(11,21): 1.2, range(21,31): 1.15, range(31,41): 1.14, range(41,51): 1.13, range(51,61): 1.12, range(61,71): 1.11, range(71,101): 1.10}
        while self.exp >= self.remainexp and self.level < 100:
            self.exp -= self.remainexp
            for level, taxa in taxes.items():
                if self.level in level:
                    tax = taxa
            self.remainexp = int(f"{(10*tax**self.level - self.level - 1):.0f}")
            self.level += 1
        return print(f"Parabéns, você subiu de nível, agora você está no nível {self.level}")
class Status:
    def __init__(self):
        self.attacks = ["soco", "golpe baixo"]
        self.health = 100
        self.atk = 1
        self.defense = 1
        self.spd = 1
        self.max_aura = 0
class ability:
    def __init__(self):
        self.effect = None
        self.cost = 100
        self.description = None
        self.name = None