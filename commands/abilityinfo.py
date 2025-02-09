from core import user
def execute():
    print(f"""Habilidade: {user.ability.name}
Custo: {user.ability.cost}
Efeito:{user.ability.effect}
Descrição: {user.ability.description}""")