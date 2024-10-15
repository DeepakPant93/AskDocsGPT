# Set the default target
.DEFAULT_GOAL := docker-run

# Run the Caddy application within a Docker container
.PHONY: docker-run
docker-run:
docker-run:
	cd caddy && \
	docker-compose -f docker-compose.yml up -d --force-recreate && \
	cd .. && \
	docker-compose -f docker-compose.yml up -d --force-recreate

