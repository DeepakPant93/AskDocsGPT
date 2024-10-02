# AskDocGPT Server

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Documentation](#documentation)

## Overview

The AskDocGPT Server is built using LangChain to train on internal documents and utilizes an open-source model from
Hugging Face to generate results. This server provides an API for processing user queries and retrieving answers from
the trained model.

## Features

- **Document Training**: Leverages LangChain to train on specified documents for improved answer generation.
- **Hugging Face Integration**: Utilizes a Hugging Face model to produce results based on user input.
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
