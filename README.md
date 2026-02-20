🚀 CLIFoundry

A dynamic, Docker-first, team-ready Python CLI starter template.

CLIFoundry is an open-source foundation for building scalable, modular CLI applications using modern Python best practices.

It is designed for:

🧑‍💻 Personal productivity

👥 Team development

🐳 Docker-first workflows

🧪 Testable architecture

🔌 Dynamic command loading

📦 Production-ready packaging

✨ Features

Dynamic command auto-discovery

Typer-based modern CLI framework

Rich terminal output

Docker development environment

Structured logging

Environment-based configuration

Pytest test suite

Ruff linting & formatting

Pre-commit integration

GitHub Actions CI-ready

📦 Project Structure
clifoundry/
│
├── src/clifoundry/
│   ├── main.py
│   ├── core/
│   ├── commands/
│   └── services/
│
├── tests/
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── pyproject.toml
🐳 Quick Start (Recommended)
1️⃣ Build Docker image
make build
2️⃣ Run health check
make health

You should see:

OK CLIFoundry is running.
3️⃣ Run tests
make test
💻 Local Development (Without Docker)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]

clifoundry health check
🧩 Adding a New Command

Create a new file inside:

src/clifoundry/commands/

Example: hello.py

import typer

app = typer.Typer()
COMMAND_NAME = "hello"


@app.command()
def say(name: str = "world"):
    print(f"Hello {name}")

That’s it.

Now available automatically:

clifoundry hello say --name Anjo

No modification to main.py required.

🏗 Architecture Principles

CLIFoundry follows these design principles:

CLI layer separated from business logic

Commands are modular

Services contain reusable logic

Configuration isolated in core

Logging centralized

Docker environment reproducible

CI ready from day one

🔧 Makefile Commands
Command	Purpose
make build	Build Docker image
make health	Run health check
make test	Run test suite
make lint	Run ruff linter
make fmt	Format code
make bash	Open Docker shell
🔐 Environment Configuration

.env example:

APP_ENV=development
DEBUG=true

Environment variables are loaded automatically inside Docker.

🧪 Testing

We use pytest.

Run:

make test

Add tests inside:

tests/
🧼 Code Quality

We use:

Ruff (linting + formatting)

Pre-commit hooks

GitHub Actions CI

Before pushing:

make lint
make fmt
make test
🧱 Recommended Command Structure

Keep commands small:

commands/
  ├── deploy.py
  ├── convert.py
  ├── backup.py

Move business logic to:

services/

This keeps CLI clean and testable.

🛠 Use Cases

CLIFoundry can power:

DevOps automation tools

File processing CLIs

Deployment helpers

Internal team tooling

SaaS admin utilities

CI/CD helpers

Cron jobs

Containerized automation scripts

🗺 Roadmap

Planned improvements:

Version command (auto-read from package metadata)

Plugin support system

Command scaffolder (new-command)

JSON logging mode

External plugin loading

Template project generator

🤝 Contributing

Contributions are welcome.

Steps:
Fork repository
Create feature branch
Run tests + lint
Submit PR

📄 License
MIT License

🏁 Why CLIFoundry?

Because you shouldn't rebuild CLI scaffolding every time.
Clone once. Build forever.