from core import user, console
from rich.panel import Panel
def execute():
    console.print(Panel(f"""[#4169E1]Nome[/#4169E1]: {user.name}
[#4169E1]Nível[/#4169E1]: {user.level}
[#4169E1]Exp para próximo nível[/#4169E1]: {user.remainexp - user.exp}
[#4169E1]Aura[/#4169E1]: {user.aura}
[#4169E1]Habilidade[/#4169E1]: {user.ability.name}
Caso deseje ver as informações de suas habilidades digite "[bold red]abilityinfo[/]" """, title="[bold red]Info", border_style="dark_blue", width=40))