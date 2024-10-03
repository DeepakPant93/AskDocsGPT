# AskDocGPT Server

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Documentation](#documentation)
- [Environment Variables](#environment-variables)
- [Setup Guide](#setup-guide)

## Overview

The AskDocGPT Server is built using LangChain to train on internal documents and utilizes the popular ChatGPT model
to generate results. This server provides an API for processing user queries and retrieving answers from the trained
model.

## Features

- **Document Training**: Leverages LangChain to train on specified documents for improved answer generation.
- **ChatGPT Integration**: Utilizes a GPT model to generate answers for user queries.
- **API**: Provides a RESTful API for interacting with the model.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DeepakPant93/AskDocsGPT.git
   cd AskDocGPT/server
   ```

2. Install the necessary packages:
   ```bash
   make install
   ```

## Running the Application

To start the application, use the following command:

```bash
make run
```

## Documentation

### API Documentation

The server includes Swagger documentation for easy exploration of the available endpoints. You can access the
documentation at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Environment Variables

Make sure to configure the following environment variables to start the server:

- `BASIC_AUTH_USERNAME=username`
- `BASIC_AUTH_PASSWORD=password`
- `LANGCHAIN_API_KEYLANGCHAIN_API_KEY=your_langchain_api_key`
- `OPENAI_API_KEY=your_openai_api_key`
- `PINECONE_API_KEY=your_pinecone_api_key`
- `PINECONE_HOST=your_pinecone_host`
- `PINECONE_INDEX_NAME=askdocs`
- `MODEL_NAME=gpt-3.5-turbo`


## Setup Guide

Please refer to the [Setup Guide](docs/SETUP.md) for a more detailed setup process.