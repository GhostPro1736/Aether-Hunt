from core import user, GameState, console
def execute():
    if GameState.isAdmin:
        try:
            gain_exp = int(input("Digite a quantidade de exp desejada: "))
            if gain_exp > 0:
                user.exp += gain_exp
                console.print(f"[#FFD700]Você recebeu[/#FFD700] [italic bold red]{gain_exp}[/italic bold red] [#FFD700]exp[/#FFD700]")
                return user.level_up()
            else:
                return print("Valor inválido, o valor não pode ser menor que 1!")
        except Exception as e:
            return print(f"Comando inválido: {e}")
    else:
        return print("Você só pode usar este comando sendo um Admin")