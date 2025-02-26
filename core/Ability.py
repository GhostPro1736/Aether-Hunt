from . import user, console, Abilities
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
import keyboard as key
from time import sleep
def get_key():
    global x
    if key.is_pressed("enter"):
        return "SELECTED"
    elif key.is_pressed("right"):
        x += 1
        if x > 3:
            x = 1
        return "PRESSIONADO"
    elif key.is_pressed("left"):
        x -=1
        if x < 1:
            x = 3
        return "PRESSIONADO"
def get_abilities():
    print(f"Você pode se mover com: esqueda, direita e para confirmar pode utilizar o enter \nSuas habilidades disponíveis para {user.aura} são:")
    abilities = {"Name": [], "Cost": [], "Effect": [], "Description": []}
    for Ability, description in Abilities[user.aura].items():
        abilities["Name"].append(Ability)
        abilities["Cost"].append(description["Custo"])
        abilities["Effect"].append(description["Efeito"])
        abilities["Description"].append(description["Descrição"])
    return abilities
def show_abilities():
    global x
    x = 1
    layout = Layout()
    title_style = ("bold orange1", "bold orange1 on white")
    layout.split_column(Layout(name='Principal'))
    habilities = get_abilities()
    layout['Principal'].split_row(
        Layout(Panel(f"[bold blue]Custo[/]: \n{habilities['Cost'][0]} \n[bold green]Efeito[/]: \n{habilities['Effect'][0]} \n[bold magenta]Descrição[/]: \n{habilities['Description'][0]}", title=f"[{title_style[1]}]{habilities['Name'][0]}[/]", border_style="Blue"), name="part1"),
        Layout(Panel(f"[bold blue]Custo[/]: \n{habilities['Cost'][1]} \n[bold green]Efeito[/]: \n{habilities['Effect'][1]} \n[bold magenta]Descrição[/]: \n{habilities['Description'][1]}", title=f"[{title_style[0]}]{habilities['Name'][1]}[/]", border_style="Blue"), name="part2"),
        Layout(Panel(f"[bold blue]Custo[/]: \n{habilities['Cost'][2]} \n[bold green]Efeito[/]: \n{habilities['Effect'][2]} \n[bold magenta]Descrição[/]: \n{habilities['Description'][2]}", title=f"[{title_style[0]}]{habilities['Name'][2]}[/]", border_style="Blue"), name="part3"))
    with Live(layout, console=console, refresh_per_second=5):
        while True:
            value = get_key()
            if value == "SELECTED":
                return
            elif value == "PRESSIONADO":
                layout['part1'].update(Panel(f"[bold blue]Custo[/]: \n{habilities['Cost'][0]} \n[bold green]Efeito[/]: \n{habilities['Effect'][0]} \n[bold magenta]Descrição[/]: \n{habilities['Description'][0]}", title=f"[{title_style[1 if x == 1 else 0]}]{habilities['Name'][0]}[/]", border_style="Blue"))
                layout['part2'].update(Panel(f"[bold blue]Custo[/]: \n{habilities['Cost'][1]} \n[bold green]Efeito[/]: \n{habilities['Effect'][1]} \n[bold magenta]Descrição[/]: \n{habilities['Description'][1]}", title=f"[{title_style[1 if x == 2 else 0]}]{habilities['Name'][1]}[/]", border_style="Blue"))
                layout['part3'].update(Panel(f"[bold blue]Custo[/]: \n{habilities['Cost'][2]} \n[bold green]Efeito[/]: \n{habilities['Effect'][2]} \n[bold magenta]Descrição[/]: \n{habilities['Description'][2]}", title=f"[{title_style[1 if x == 3 else 0]}]{habilities['Name'][2]}[/]", border_style="Blue"))
                sleep(0.2)
def choose_ability():
    show_abilities()
    while True:
            abilities = list(Abilities[user.aura].items())
            if x in range(1, len(abilities)+1):
                chosen_ability, description = abilities[x - 1]
                user.ability.update_all(cost=description['Custo'], effect=description["Efeito"], name=chosen_ability, description=description["Descrição"])
                return print(f"\nÓtima escolha, agora sua habilidade permanente é: {chosen_ability}")
            else:
                print("\nPor favor coloque o número de sua habilidade desejada:\n", end="\n")
                show_abilities()
def debug_show_abilities():
    habilities = {"Name": [], "Cost": [], "Effect": [], "Description": []}
    for Ability, description in Abilities[user.aura].items():
        habilities["Name"].append(Ability)
        habilities["Cost"].append(description["Custo"])
        habilities["Effect"].append(description["Efeito"])
        habilities["Description"].append(description["Descrição"])
def debug_choose_ability():
    debug_show_abilities()
    abilities = list(Abilities[user.aura].items())
    chosen_ability, description = abilities[2]
    user.ability.update_all(cost=description['Custo'], effect=description["Efeito"], name=chosen_ability, description=description["Descrição"])