# CLIFoundry

[![CI](https://github.com/anjotadena/clifoundry/actions/workflows/ci.yml/badge.svg)](https://github.com/anjotadena/clifoundry/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/anjotadena/clifoundry)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

![CLIFoundry logo](./assets/clifoundry.png)

Docker-first, dynamic, team-ready Python CLI starter template with built-in scaffolding.

## ✨ What this template includes

- **Dynamic command loading** - commands are auto-discovered from `commands/` directory
- **Built-in scaffolding** - generate commands, services, and tests with one command
- **Docker-first workflow** - Make targets for common tasks
- **Rich CLI output** - colorful, formatted output using Rich
- **Test suite** - pytest setup ready to go
- **Type hints** - full type annotations for better IDE support
- **Service layer pattern** - clean separation of business logic

## Prerequisites

### Docker-first (recommended)

- Docker Engine 24+ (or Docker Desktop)
- Docker Compose v2
- Make

Windows note: Docker Desktop for Windows includes Docker Engine and Compose. Make is not included by default.

### Local Python (optional)

- Python 3.10+
- pip (bundled with Python)
- Make (optional, but convenient)

## Quickstart (Docker)

```bash
# Build the Docker image
make build

# Run health check
make health

# Run tests
make test

# See all available commands
docker compose run --rm cli clifoundry --help
```

## 🚀 Scaffolding - Generate New Components

CLIFoundry includes powerful scaffolding to quickly create new commands, services, and tests.

### Generate a new command

```bash
# Using the CLI directly
docker compose run --rm cli clifoundry generate command my-feature --desc "My feature description"

# Or using the Makefile shortcut
make gen-cmd name=my-feature desc="My feature description"
```

This creates a fully functional command file at `src/clifoundry/commands/my_feature.py` with:
- Proper imports and structure
- Example command with options
- Rich formatting
- Auto-registration (no manual setup needed!)

### Generate a new service

```bash
# Using the CLI directly
docker compose run --rm cli clifoundry generate service user --desc "User management service"

# Or using the Makefile shortcut
make gen-service name=user desc="User management service"
```

This creates a service class at `src/clifoundry/services/user.py` with:
- Full type hints
- CRUD methods (get, create, update, delete)
- Comprehensive docstrings
- Ready to import into your commands

### Generate tests for a command

```bash
# Using the CLI directly
docker compose run --rm cli clifoundry generate test my-feature

# Or using the Makefile shortcut
make gen-test name=my-feature
```

This creates test file at `tests/test_my_feature.py` with:
- Three test cases (help, run, with options)
- CliRunner setup
- Proper assertions

## Setup and usage

### Build the image

```bash
make build
```

### Run the CLI

```bash
# Run any command
docker compose run --rm cli clifoundry <command>

# Examples
docker compose run --rm cli clifoundry hello say --name "World"
docker compose run --rm cli clifoundry info show
docker compose run --rm cli clifoundry health check

# Interactive shell
make bash
```

### Run tests

```bash
make test              # Run all tests (quiet mode)
make lint              # Check code style
make fmt               # Format code
```

## Example: Creating a complete feature

Here's how to create a complete feature with command, service, and tests:

```bash
# 1. Generate a service for business logic
make gen-service name=task desc="Task management service"

# 2. Generate a command that uses the service
make gen-cmd name=tasks desc="Task management commands"

# 3. Edit the command to import and use the service
# (Edit src/clifoundry/commands/tasks.py to import from services.task)

# 4. Generate tests
make gen-test name=tasks

# 5. Run your new command
docker compose run --rm cli clifoundry tasks --help

# 6. Run the tests
docker compose run --rm cli pytest tests/test_tasks.py -v
```

## Local Python workflow (no Docker)

If you prefer to run locally, create a virtual environment and install the package.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

Windows (cmd):

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -e .
```

Then run the CLI.

```bash
clifoundry --help
clifoundry generate --help
clifoundry generate command my-cmd --desc "My command"
clifoundry hello say
clifoundry info show
clifoundry health check
```

Run tests locally.

```bash
pytest
pytest -v  # verbose mode
pytest tests/test_health.py  # specific test file
```

## Project layout

```
src/clifoundry/
  main.py              CLI entry point with dynamic command loading
  commands/
    __init__.py
    hello.py           Example command
    health.py          Health check commands
    info.py            Config/environment info
    generate.py        Scaffolding generator commands ⭐
    user_mgmt.py       Example service integration
  core/
    __init__.py
    config.py          Configuration management
    logging.py         Logging setup
  services/
    __init__.py
    user.py            Example service with CRUD operations
tests/
  test_health.py       Health check tests
  test_hello_world.py  Generated test example
```

## Available Commands

Run `docker compose run --rm cli clifoundry --help` to see all commands:

- **hello** - Simple greeting command
- **health** - Health checks and diagnostics
- **info** - Show environment/config info
- **generate** - Scaffold new commands, services, and tests ⭐
- **user-mgmt** - Example of command+service integration

## Makefile Shortcuts

```bash
make build          # Build Docker image
make bash           # Open bash shell in container
make run            # Run CLI interactively
make health         # Run health check
make info           # Show config info
make test           # Run tests
make lint           # Run linter
make fmt            # Format code

# Scaffolding shortcuts
make gen-cmd name=mycommand desc="Description"
make gen-service name=myservice desc="Description"
make gen-test name=mycommand
```

## Customizing

### Adding a new command manually

1. Create a new file in `src/clifoundry/commands/` (e.g., `my_command.py`)
2. Use this structure:

```python
import typer
from rich import print

app = typer.Typer(help="My command description")
COMMAND_NAME = "my-command"

@app.command()
def run():
    """Run my command."""
    print("[green]Hello from my command![/green]")
```

3. The command is automatically discovered and registered!
4. Test it: `docker compose run --rm cli clifoundry my-command --help`

### Or use the generator (recommended)

```bash
make gen-cmd name=my-command desc="My command description"
```

## Continuous Integration

CLIFoundry uses GitHub Actions for continuous integration. Every push and pull request automatically:

- ✅ **Lints code** with Ruff (`ruff check .`)
- ✅ **Checks formatting** with Ruff (`ruff format --check .`)
- ✅ **Runs test suite** with pytest (`pytest -q`)

### CI Workflow

The CI workflow is defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) and runs on Python 3.12.

### Running CI Checks Locally

You can run the same checks locally before pushing:

```bash
# Docker (recommended)
make lint      # Run linting
make fmt       # Format code
make test      # Run tests

# Or all at once
make lint && make fmt && make test

# Local Python
ruff check .
ruff format .
pytest
```

### CI Status

Check the [Actions tab](https://github.com/anjotadena/clifoundry/actions) for the latest CI runs and results.

## Main contributor

- Anjo Tadena

## Troubleshooting

- If Docker build fails, ensure the Docker daemon is running and you have Compose v2
- If local imports fail, confirm the virtual environment is active and `pip install -e .` ran
- If a command doesn't appear, check that your file has `app = typer.Typer()` and `COMMAND_NAME` defined
- Use `make bash` to explore inside the container for debugging
