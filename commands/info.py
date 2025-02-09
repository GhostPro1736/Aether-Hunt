from core import user
def execute():
    print(f"""Nome: {user.name}
Nível: {user.level}
Exp restante para próximo nível: {user.remainexp - user.exp}
Aura: {user.aura}
Habilidade: {user.ability.name}
Caso deseje ver as informações de suas habilidades digite "abilityinfo" """)
