from core import user
def execute():
    attacks = ", ".join(user.status.attacks)
    print(f"""Status gerais:
Ataques disponíveis: {attacks}
Vida atual: {user.status.health}
Ataque base: {user.status.atk}
Defesa base: {user.status.defense}
Velocidade base: {user.status.spd}
Aura máxima {user.status.max_aura}""")