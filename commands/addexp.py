from core import user, GameState, random_color
def execute():
    if GameState.isAdmin:
        try:
            gain_exp = int(input("Digite a quantidade de exp desejada: "))
            if gain_exp > 0:
                user.exp += gain_exp
                print(random_color(f"Você recebeu {gain_exp} exp"))
                return user.level_up()
            else:
                return print("Valor inválido, o valor não pode ser menor que 1!")
        except Exception as e:
            return print(f"Comando inválido: {e}")
    else:
        return print("Você só pode usar este comando sendo um Admin")