# CLIFoundry

![CLIFoundry logo](./assets/clifoundry.png)

Docker-first, dynamic, team-ready Python CLI starter template.

## What this template includes

- A minimal CLI app with subcommands and health checks.
- Docker-first workflow with Make targets for common tasks.
- A small test suite to validate behavior.

## Prerequisites

### Docker-first (recommended)

- Docker Engine 24+ (or Docker Desktop).
- Docker Compose v2.
- Make.

Windows note: Docker Desktop for Windows includes Docker Engine and Compose. Make is not included by default.

### Local Python (optional)

- Python 3.11+.
- pip (bundled with Python).
- Make (optional, but convenient).

## Quickstart (Docker)

```bash
make build
make health
make test
```

## Setup and usage

### Build the image

```bash
make build
```

### Run the CLI

```bash
make hello
make info
make health
```

### Run tests

```bash
make test
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
clifoundry hello
clifoundry info
clifoundry health
```

Run tests locally.

```bash
pytest
```

## Project layout

```
src/clifoundry/
  main.py          CLI entry point
  commands/        CLI subcommands
  core/            shared utilities (config, logging)
tests/             test suite
```

## Customizing

- Add a new command by creating a module in src/clifoundry/commands/.
- Register the command in the CLI entry point.
- Add tests in tests/.

## Main contributor

- Anjo Tadena

## Troubleshooting

- If Docker build fails, ensure the Docker daemon is running and you have Compose v2.
- If local imports fail, confirm the virtual environment is active and pip install -e . ran.
