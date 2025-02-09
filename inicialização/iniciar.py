from pyfiglet import figlet_format
from colorama import Fore, init
def title():
    init(autoreset=True)
    f = figlet_format("Aether Hunt",font="wet_letter", justify="right")
    print(Fore.LIGHTGREEN_EX + f)
    inicio = input(f"Digite iniciar para começar: ")
    if inicio.lower() == "iniciar":
        return True