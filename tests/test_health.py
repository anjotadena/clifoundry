from typer.testing import CliRunner
from clifoundry.main import app

runner = CliRunner()


def test_health_check():
    result = runner.invoke(app, ["health", "check"])
    assert result.exit_code == 0
    assert "OK" in result.stdout