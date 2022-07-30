.PHONY: build, shell, poetry

build:
	@.scripts/docker-build.sh

shell:
	@docker compose run shell

poetry:
	@.scripts/docker-poetry.sh
