# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


import base64
from typing import Dict

import requests

from ..core.config import settings
from ..core.context import request_id_context
from ..core.logger import logger
from ..schema.v1.prompt_schema import AnswerResponse


# import httpx


class AskDocsAPIProxy:
    def __init__(self):
        self.base_url = settings.ASK_DOCS_SERVER_BASE_URL.rstrip('/') + '/api/v1'
        self.auth_header = self._create_auth_header(settings.ASK_DOCS_SERVER_BASIC_AUTH_USERNAME,
                                                    settings.ASK_DOCS_SERVER_BASIC_AUTH_PASSWORD)
        self.headers = {
            "Authorization": self.auth_header,
            "X-Request-ID": request_id_context.get(None)
        }

    def _create_auth_header(self, username: str, password: str) -> str:
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded_credentials}"

    async def ask(self, request: str) -> AnswerResponse:
        try:
            response = requests.post(
                url=f"{self.base_url}/docs/ask",
                headers=self.headers,
                json={'question': request})
            return AnswerResponse(**response.json())
        except Exception as e:
            logger.error(f"Failed to get answer from ask-docs backend service: {e}")
            raise

    @staticmethod
    async def health_check() -> Dict[str, str]:
        try:
            health_check_url = settings.ASK_DOCS_SERVER_BASE_URL.rstrip('/') + '/health'
            response = requests.get(health_check_url)
            logger.info(f"Health check passed for ask-docs backend service")
            return response.json()
        except Exception as e:
            logger.error(f"Failed to check health for ask-docs backend service: {e}")
            return {"status": "unhealthy"}
