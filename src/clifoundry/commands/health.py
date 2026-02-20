import typer
from rich import print

app = typer.Typer(help="Health checks and diagnostics.")
COMMAND_NAME = "health"


@app.command()
def check() -> None:
    """Simple health check."""
    print("[green]OK[/green] CLIFoundry is running.")
