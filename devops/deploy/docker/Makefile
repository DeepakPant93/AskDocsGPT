# Set the default target
.DEFAULT_GOAL := docker-run

# Run the Caddy application within a Docker container
.PHONY: docker-run
docker-run:
	docker-compose -f caddy/docker-compose.yml up -d --force-recreate
	docker-compose -f docker-compose.yml up -d --force-recreate
