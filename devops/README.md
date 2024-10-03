# AskDocsGPT DevOps Overview

## Overview
The DevOps folder contains the configuration files required to deploy the AskDocGPT application using Docker. The primary component is the `docker-compose.yml` file, which defines the services for both the client and the server, facilitating easy deployment and management of the application.

## Docker Compose Configuration
The `docker-compose.yml` file defines the following services:

1. **ask_docs_client**: Runs the client application that interacts with the server's APIs.
2. **ask_docs_server**: Runs the server application that handles requests and interfaces with the GPT model to provide answers.

## Pre-requisites

To successfully run the AskDocGPT application, you must have the following:

1. **OpenAI API Keys**: Required for GPT-based responses. You can obtain it from [OpenAI API Keys](https://platform.openai.com/api-keys).
   
2. **Langchain API Key**: Required for LangChain functionality. You can acquire it from [Langchain API Key](https://smith.langchain.com/o/da94479a-d90e-569a-bc3f-19bd892df75a/settings).

3. **Pinecone API Key**: Required for vector database integration. You can get it from [Pinecone API Key](https://app.pinecone.io/organizations/-O8DZPZ8uMFcn4dg1MMa/projects/281d40c0-d2ec-4932-949f-b3345d58f52b/keys).

4. **Pinecone Index**: Create an index in Pinecone with the following specifications:
   - Index Name: `askdocs`
   - Dimension: `1536`

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
```