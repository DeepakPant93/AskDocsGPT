# Set the default target
.DEFAULT_GOAL := run

# Variables
IMAGE_NAME = deepak93p/ask-docs-server
TAG = latest
PLATFORMS = linux/amd64,linux/arm64
DOCKERFILE = Dockerfile
BUILD_DIR = .
TEST_DIR=tests
TEST_RUNNER=pytest


.PHONY: all
all: build

# Create and use buildx builder (if not already created)
.PHONY: setup
setup:
	@docker buildx create --name multiarch-builder --use || echo "Builder already exists"

# Build the Docker image for multiple platforms
.PHONY: build
build: setup
	@docker buildx build --platform $(PLATFORMS) -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE) $(BUILD_DIR)

# Build and push the image to the registry
.PHONY: build-and-push
build-and-push: setup
	@docker buildx build --platform $(PLATFORMS) -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE) $(BUILD_DIR) --push

# Clean up the buildx builder
.PHONY: clean
clean:
	@docker buildx rm multiarch-builder || echo "No builder to remove"
	docker rmi $(IMAGE_NAME):$(TAG)
	docker network prune -f

# Setup for virtual environment and install the application requirements
.PHONY: venv
venv:
	conda create --name .venv python=3.10 -y && \
	conda init && \
	conda activate .venv


# Activate the virtual environment
.PHONY: venv-activate
venv-activate:
	conda init && conda activate .venv


# Destroy the virtual environment
.PHONY: destroy-venv
destroy-venv:
	conda deactivate && \
	rm -rf .venv

# Run the application
.PHONY: run
run:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload


# Install the application requirements
.PHONY: install
install:
	pip install -r requirements.txt


# Run the Emailer_Worker application within a Docker container
.PHONY: docker-run
docker-run:
	docker-compose -f docker-compose.yml up -d --force-recreate

# Run the test cases
.PHONY: test
test:
	$(TEST_RUNNER) $(TEST_DIR)