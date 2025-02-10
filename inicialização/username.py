from core import user
def name():
    while True:
        nome = input("Digite seu nome de usuário, Min 3 caracteres, Máx 15 caracteres: ")
        if len(nome) < 3:
            print("Por favor insira um nome de usuário válido")
        elif len(nome) > 15:
            print("Seu nome é grande demais, por favor, insira um nome mais curto")
        else:
            user.name = nome
            return print(f"Ótimo {nome}, sua jornada começa agora, vamos ver agora seu tipo de aura")