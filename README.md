# AskDocGPT

## Description

AskDocGPT is a GPT-powered system designed to answer questions from internal documents. It provides concise answers with
direct links to relevant sources for easy verification, enhancing the efficiency of information retrieval and knowledge
sharing.

## Table of Contents

- [Components](#components)
- [Technical documents](#technical-documents)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Development](#development)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Components

### Server

The server component is responsible for handling requests and interfacing with the GPT model to generate answers based
on internal documents.

- **[Server README](./server/README.md)**

### Client

The client component provides the user interface for the application, allowing users to input questions and view answers
generated by the server.

- **[Client README](./client/README.md)**

### DevOps

The devops folder contains the necessary configuration files for deployment, including Dockerfiles and scripts for
setting up the application in various environments.

- **[DevOps README](./devops/README.md)**

## Technical documents

- For a detailed overview of the application's architecture, please see the [Architecture](docs/architecture.md)
  document.
- For a detailed overview of the technical report, please visit [Technical Report](docs/technical-report.md)

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic understanding of Docker and API interactions.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DeepakPant93/AskDocsGPT.git
   cd AskDocGPT
   ```

2. Build and start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Environment Variables

Make sure to set the following environment variables before running the application:

- For **ask_docs_client**:
    - `NAME=ask-docs-client`
    - `ASK_DOCS_SERVER_BASIC_AUTH_USERNAME=askdocs-user`
    - `ASK_DOCS_SERVER_BASIC_AUTH_PASSWORD=askdocs-password`
    - `ASK_DOCS_SERVER_BASE_URL=http://ask_docs_server:8000`

- For **ask_docs_server**:
    - `BASIC_AUTH_USERNAME=username`
    - `BASIC_AUTH_PASSWORD=password`
    - `LANGCHAIN_API_KEY=your_langchain_api_key`
    - `OPENAI_API_KEY=your_openai_api_key`
    - `PINECONE_API_KEY=your_pinecone_api_key`
    - `PINECONE_INDEX_NAME=askdocs`
    - `MODEL_NAME=gpt-3.5-turbo`

## Development

- Use the appropriate IDE or code editor for your component (e.g., Python for the server and client).
- Ensure your code adheres to the project's coding standards.

## Deployment

The application is deployed on an AWS EC2 instance. You can access it using the following links:

- **[Backend Server](https://ec2-65-1-108-185.ap-south-1.compute.amazonaws.com/docs#)**
- **[Client App](https://ec2-65-1-108-185.ap-south-1.compute.amazonaws.com/)**

Use the blow credentials to access the backend server:

```commandline
Username: askdocs-user
Password: askdocs-password
```

The data available in the database is from the test data located in the [test/test-data](test/test-data) folder, and you
can ask questions like:

- What is the name of the captain?
- Who is the captain's dog?
- Who is James's sister?
- Who is James's BFF?

## Usage

- Access the client interface through your web browser
  at [here](https://ec2-65-1-108-185.ap-south-1.compute.amazonaws.com).
- Enter your queries in the UI to receive answers sourced from the internal documents.

## License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.