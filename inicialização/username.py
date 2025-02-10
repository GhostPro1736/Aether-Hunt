from core import user, console
from rich.prompt import Prompt
def name():
    while True:
        nome = Prompt.ask("[b white]Digite seu nome de usuário[/], Min 3 caracteres, Máx 15 caracteres")
        if len(nome) < 3:
            console.print("Por favor insira um nome de usuário [b]válido[/]")
        elif len(nome) > 15:
            console.print("Seu nome é [b]grande demais[/], por favor, insira um nome mais curto")
        else:
            user.name = nome
            return console.print(f"Ótimo [bold yellow]{nome}[/], sua jornada começa agora, vamos ver agora [bold #00008B]seu tipo de aura[/]")