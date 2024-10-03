# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


from pydantic import BaseSettings


class Settings(BaseSettings):
    # Settings for basic auth
    BASIC_AUTH_USERNAME: str
    BASIC_AUTH_PASSWORD: str

    # Settings for OpenAI
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-3.5-turbo"
    TEMPERATURE: float = 0.5
    MAX_TOKENS: int = 200

    # Settings for Langchain
    LANGCHAIN_API_KEY: str

    ## Settings for Pinecone
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str = "askdocs"

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 20

    ## Other settings
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

    class Config:
        env_file = ".env"


settings = Settings()
