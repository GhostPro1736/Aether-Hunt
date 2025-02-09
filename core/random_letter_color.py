import random
from colorama import Fore
def random_color(mens):
    mensage = ""
    colors = (Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.WHITE, Fore.LIGHTBLACK_EX, Fore.MAGENTA, Fore.LIGHTRED_EX)
    for letter in mens:
        color = random.choice(colors)
        mensage += f"{color}{letter}"
    return mensage