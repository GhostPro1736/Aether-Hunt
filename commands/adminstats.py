from core import GameState
tentativas = 5
def execute():
    global tentativas
    if GameState.isAdmin:
        print("Você já é um administrador!")
    else:
        if tentativas >0:
            try:
                passwords = (930740,142926,888790,497338,875830,679072,618296,988890,728672,834610)
                password = int(input("Digite a senha para se tornar um admin: "))
                if password in passwords:
                    GameState.isAdmin = True
                    return print("Você se tornou um administrador, agora você pode usar comandos especiais")
                else:
                    tentativas -= 1
                    return print("Senha inválida!")
            except Exception as e:
                tentativas -= 1
                return print(f"Erro, senha inválida, motivo: {e}")