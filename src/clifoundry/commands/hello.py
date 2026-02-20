import typer
app = typer.Typer()
COMMAND_NAME = "hello"

@app.command()
def say(name: str = "world"):
    print(f"Hello {name}")