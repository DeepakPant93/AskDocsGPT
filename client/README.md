# AskDocGPT Client

## Description

The AskDocGPT Client is a user-friendly interface designed to interact with the AskDocGPT server, providing a
ChatGPT-like chatting console. This application utilizes Streamlit to create a dynamic and responsive UI for users to
input their queries and receive answers sourced from internal documents.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)

## Features

- Intuitive chatting interface similar to ChatGPT.
- Real-time responses from the AskDocGPT server.
- Easy to deploy and run using Streamlit.

## Getting Started

### Prerequisites

- Python 3.10 or higher installed on your machine.
- Basic knowledge of Python and API interactions.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DeepakPant93/AskDocsGPT.git
   cd AskDocGPT/client
   ```

2. Install the required dependencies:
   ```bash
   make install
   ```

3. Ensure that the AskDocGPT server is running and accessible on port 8000.

## Usage

1. Start the Streamlit application:
   ```bash
   make run
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8502
   ```
   (or the appropriate port if you've configured it differently).

3. Enter your queries in the chat console and press Enter to receive answers from the server.

## Environment Variables

Make sure to configure the following environment variables for connecting to the AskDocGPT server:

- `ASK_DOCS_SERVER_BASIC_AUTH_USERNAME=username`
- `ASK_DOCS_SERVER_BASIC_AUTH_PASSWORD=password`
- `ASK_DOCS_SERVER_BASE_URL=http://ask_docs_server:8000` (or the appropriate URL if hosted elsewhere)
