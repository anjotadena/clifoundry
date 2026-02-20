import importlib
import pkgutil
from pathlib import Path

import typer

from clifoundry.core.logging import setup_logging

app = typer.Typer(help="CLIFoundry — dynamic, Docker-first CLI starter template.")
setup_logging()


def load_commands() -> None:
    package = "clifoundry.commands"
    package_path = Path(__file__).parent / "commands"

    for _, module_name, is_pkg in pkgutil.iter_modules([str(package_path)]):
        if is_pkg:
            continue

        module = importlib.import_module(f"{package}.{module_name}")

        # Each command module should expose `app = typer.Typer(...)`
        cmd_app = getattr(module, "app", None)
        if cmd_app is not None:
            command_name = getattr(module, "COMMAND_NAME", module_name.replace("_", "-"))
            app.add_typer(cmd_app, name=command_name)


load_commands()
