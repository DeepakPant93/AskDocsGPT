# Setup Guide for AskDocGPT

This document outlines the steps to set up the AskDocGPT application using Makefile commands.

## Makefile Commands

### 1. `make venv`
Create a virtual environment named `.venv` with Python 3.10.

### 2. `make destroy-venv`
Destroy the virtual environment named `.venv` if it exists.

### 3. `make install`
Install the required Python packages listed in `requirements.txt`.

### 4. `make run`
Run the application using Uvicorn on port 8000 with live reload enabled.

### 5. `make build`
Create and use a Docker Buildx builder (if not already created) and build the Docker image for multiple platforms.

### 6. `make build-and-push`
Build the Docker image for multiple platforms and push it to the Docker registry.

### 7. `make clean`
Clean up the buildx builder and remove the Docker image and unused networks.

### 8. `make docker-run`
Run the Emailer_Worker application within a Docker container using Docker Compose.

## Additional Notes

- Ensure you have the required software installed (Docker, Docker Compose, Conda, and Python).
- For more details on specific commands, refer to the Makefile in the root directory of the project.