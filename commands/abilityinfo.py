from core import user, console
def execute():
    console.print(f"""[#4169E1]Habilidade[/#4169E1]: {user.ability.name}
[#4169E1]Custo[/#4169E1]: {user.ability.cost}
[#4169E1]Efeito[/#4169E1]:{user.ability.effect}
[#4169E1]Descrição[/#4169E1]: {user.ability.description}""")