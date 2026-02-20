build:
	docker compose build

bash:
	docker compose run --rm cli bash

run:
	docker compose run --rm cli

health:
	docker compose run --rm cli clifoundry health check

info:
	docker compose run --rm cli clifoundry info show

test:
	docker compose run --rm cli pytest -q

lint:
	docker compose run --rm cli ruff check .

fmt:
	docker compose run --rm cli ruff format .