# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


from pydantic import BaseSettings


class Settings(BaseSettings):
    # Settings for basic auth
    BASIC_AUTH_USERNAME: str
    BASIC_AUTH_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()
