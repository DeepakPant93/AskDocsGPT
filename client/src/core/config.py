# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

import os

from dotenv import load_dotenv


class Settings:
    # Load .env file
    load_dotenv()

    # Settings for basic auth
    ASK_DOCS_SERVER_BASIC_AUTH_USERNAME: str = os.environ["ASK_DOCS_SERVER_BASIC_AUTH_USERNAME"]
    ASK_DOCS_SERVER_BASIC_AUTH_PASSWORD: str = os.environ["ASK_DOCS_SERVER_BASIC_AUTH_PASSWORD"]
    ASK_DOCS_SERVER_BASE_URL: str = os.environ["ASK_DOCS_SERVER_BASE_URL"]

    MIN_INPUT_LENGTH: int = 3
    MAX_INPUT_LENGTH: int = 250

    class Config:
        env_file = ".env"


settings = Settings()
