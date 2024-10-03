# DevOps Folder README

## Overview
The DevOps folder contains the configuration files required to deploy the AskDocGPT application using Docker. The primary component is the `docker-compose.yml` file, which defines the services for both the client and the server, facilitating easy deployment and management of the application.

## Docker Compose Configuration
The `docker-compose.yml` file defines the following services:

1. **ask_docs_client**: Runs the client application that interacts with the server's APIs.
2. **ask_docs_server**: Runs the server application that handles requests and interfaces with the GPT model to provide answers.

### Environment Variables
To run the services, you need to create a `.env` file with the following content. Replace the placeholder values with your actual configuration:

```plaintext
# Basic Auth credentials
SERVER_BASIC_AUTH_USERNAME=your_username_here
SERVER_BASIC_AUTH_PASSWORD=your_password_here

# API Keys
LANGCHAIN_API_KEY=your_langchain_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here

# Pinecone Host
PINECONE_HOST=your_pinecone_host_here
```

### Health Check
The server service includes a health check to ensure it is operational. It performs a check every 30 seconds to confirm that the server is accessible.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation
1. Navigate to the `devops` folder:
   ```bash
   cd devops
   ```

2. Create a `.env` file with the necessary variables (see the Environment Variables section above).

3. Start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Access the client interface in your web browser at `http://localhost:8502`.

### Stopping the Services
To stop the services, run:
```bash
docker-compose down
```

## Troubleshooting
If you encounter any issues, check the logs for each service by running:
```bash
docker-compose logs
