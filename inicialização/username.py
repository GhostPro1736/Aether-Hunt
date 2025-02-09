from core import user
def name():
    while user.name == None:
        nome = input("Digite seu nome de usuário, Min 3 caracteres, Máx 15 caracteres: ")
        if len(nome) < 3:
            return "Por favor insira um nome de usuário válido"
        elif len(nome) > 15:
            return "Seu nome é grande demais, por favor, insira um nome mais curto"
        else:
            user.name = nome
            return f"Ótimo {nome}, sua jornada começa agora, vamos ver agora seu tipo de aura"