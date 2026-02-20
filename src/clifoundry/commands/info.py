import typer
from rich import print

from clifoundry.core.config import settings

app = typer.Typer(help="Show environment/config info.")
COMMAND_NAME = "info"


@app.command()
def show() -> None:
    print(f"[cyan]env[/cyan]: {settings.env}")
    print(f"[cyan]debug[/cyan]: {settings.debug}")
