.PHONY: build, shell

build:
	@.scripts/docker-build.sh

shell:
	@docker compose run shell
