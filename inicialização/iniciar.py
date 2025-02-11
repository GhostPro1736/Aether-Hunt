from pyfiglet import figlet_format
from core import console
from rich.panel import Panel
from rich.prompt import Prompt
def title():
    f = figlet_format("Aether Hunt",font="wet_letter", justify="left")
    panel = Panel(f"[bold #02d8e9]{f}[/bold #02d8e9]", border_style="#4B0082", expand=False)
    console.print(panel)
    inicio = Prompt.ask(f"[bold red]Digite iniciar para começar[/bold red]", default="iniciar", show_default=False)
    if inicio.lower() == "iniciar":
        return True