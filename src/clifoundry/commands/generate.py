from pathlib import Path

import typer
from rich import print

app = typer.Typer(help="Generate and scaffold new commands.")
COMMAND_NAME = "generate"


@app.command()
def command(
    name: str = typer.Argument(..., help="Name of the command to generate (e.g., 'hello')"),
    description: str = typer.Option(
        "Command description.", "--desc", "-d", help="Description for the command"
    ),
) -> None:
    """Generate a new command file with boilerplate code."""

    # Normalize the command name
    command_name = name.lower().replace("-", "_")
    file_name = f"{command_name}.py"

    # Get the commands directory path
    commands_dir = Path(__file__).parent
    file_path = commands_dir / file_name

    # Check if file already exists
    if file_path.exists():
        print(f"[red]Error:[/red] Command file '{file_name}' already exists!")
        raise typer.Exit(1)

    # Generate the command template
    template = f'''import typer
from rich import print

app = typer.Typer(help="{description}")
COMMAND_NAME = "{name.lower().replace("_", "-")}"


@app.command()
def run(
    name: str = typer.Option("world", "--name", "-n", help="Name to greet")
) -> None:
    """Run the {name} command."""
    print(f"[green]Hello[/green] {{name}} from [cyan]{name}[/cyan] command!")
'''

    # Write the file
    file_path.write_text(template)

    print(f"[green]✓[/green] Generated command: [cyan]{file_name}[/cyan]")
    print(f"[dim]Location:[/dim] {file_path}")
    print("")
    print("[yellow]Next steps:[/yellow]")
    print(f"  1. Edit [cyan]{file_path}[/cyan] to customize your command")
    print(f"  2. Run: [dim]clifoundry {name.lower().replace('_', '-')} --help[/dim]")


@app.command()
def service(
    name: str = typer.Argument(..., help="Name of the service to generate (e.g., 'user')"),
    description: str = typer.Option(
        "Service description.", "--desc", "-d", help="Description for the service"
    ),
) -> None:
    """Generate a new service class with boilerplate code."""

    # Normalize the service name
    service_name = name.lower().replace("-", "_")
    file_name = f"{service_name}.py"
    class_name = "".join(word.capitalize() for word in service_name.split("_")) + "Service"

    # Get the services directory path
    services_dir = Path(__file__).parent.parent / "services"
    file_path = services_dir / file_name

    # Check if file already exists
    if file_path.exists():
        print(f"[red]Error:[/red] Service file '{file_name}' already exists!")
        raise typer.Exit(1)

    # Generate the service template
    template = f'''"""
{description}
"""
from typing import Any


class {class_name}:
    """
    {class_name} handles {service_name} related operations.
    """

    def __init__(self) -> None:
        """Initialize the {service_name} service."""
        pass

    def get(self, id: str) -> dict[str, Any]:
        """
        Get {service_name} by ID.
        
        Args:
            id: The {service_name} identifier
            
        Returns:
            Dictionary containing {service_name} data
        """
        # TODO: Implement logic
        return {{"id": id, "status": "active"}}

    def create(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Create a new {service_name}.
        
        Args:
            data: The {service_name} data
            
        Returns:
            Dictionary containing created {service_name} data
        """
        # TODO: Implement logic
        return {{"id": "new_id", **data}}

    def update(self, id: str, data: dict[str, Any]) -> dict[str, Any]:
        """
        Update an existing {service_name}.
        
        Args:
            id: The {service_name} identifier
            data: The updated {service_name} data
            
        Returns:
            Dictionary containing updated {service_name} data
        """
        # TODO: Implement logic
        return {{"id": id, **data}}

    def delete(self, id: str) -> bool:
        """
        Delete a {service_name}.
        
        Args:
            id: The {service_name} identifier
            
        Returns:
            True if successful
        """
        # TODO: Implement logic
        return True
'''

    # Write the file
    file_path.write_text(template)

    print(f"[green]✓[/green] Generated service: [cyan]{file_name}[/cyan]")
    print(f"[dim]Location:[/dim] {file_path}")
    print(f"[dim]Class:[/dim] {class_name}")
    print("")
    print("[yellow]Next steps:[/yellow]")
    print(f"  1. Edit [cyan]{file_path}[/cyan] to implement your service logic")
    print(
        f"  2. Import in your command: [dim]from clifoundry.services.{service_name} import {class_name}[/dim]"
    )


@app.command()
def test(
    command_name: str = typer.Argument(..., help="Name of the command to test (e.g., 'hello')"),
) -> None:
    """Generate a test file for a command."""

    # Normalize the command name
    cmd_name = command_name.lower().replace("-", "_")
    file_name = f"test_{cmd_name}.py"

    # Get the tests directory path
    project_root = Path(__file__).parent.parent.parent.parent
    tests_dir = project_root / "tests"
    file_path = tests_dir / file_name

    # Check if file already exists
    if file_path.exists():
        print(f"[red]Error:[/red] Test file '{file_name}' already exists!")
        raise typer.Exit(1)

    # Generate the test template
    template = f'''from typer.testing import CliRunner
from clifoundry.main import app

runner = CliRunner()


def test_{cmd_name}_help():
    """Test {command_name} command help."""
    result = runner.invoke(app, ["{command_name.lower().replace("_", "-")}", "--help"])
    assert result.exit_code == 0
    assert "{command_name.lower().replace("_", "-")}" in result.stdout.lower()


def test_{cmd_name}_run():
    """Test {command_name} command execution."""
    result = runner.invoke(app, ["{command_name.lower().replace("_", "-")}", "run"])
    assert result.exit_code == 0
    # TODO: Add more specific assertions


def test_{cmd_name}_with_options():
    """Test {command_name} command with custom options."""
    result = runner.invoke(app, ["{command_name.lower().replace("_", "-")}", "run", "--name", "test"])
    assert result.exit_code == 0
    assert "test" in result.stdout
'''

    # Write the file
    file_path.write_text(template)

    print(f"[green]✓[/green] Generated test: [cyan]{file_name}[/cyan]")
    print(f"[dim]Location:[/dim] {file_path}")
    print("")
    print("[yellow]Next steps:[/yellow]")
    print(f"  1. Edit [cyan]{file_path}[/cyan] to add specific test cases")
    print(f"  2. Run tests: [dim]make test[/dim] or [dim]pytest tests/{file_name}[/dim]")
