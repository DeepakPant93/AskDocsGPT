# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


import base64
from typing import Dict

from aiohttp import ClientSession

from ..core.config import settings
from ..core.context import request_id_context
from ..core.logger import logger
from ..schema.v1.prompt_schema import AnswerResponse


class AskDocsAPIProxy:
    def __init__(self):
        self.base_url = settings.ASK_DOCS_SERVER_BASE_URL.rstrip('/') + '/api/v1'
        self.health_check_url = settings.ASK_DOCS_SERVER_BASE_URL.rstrip('/') + '/health'
        self.auth_header = self._create_auth_header(settings.ASK_DOCS_SERVER_BASIC_AUTH_USERNAME,
                                                    settings.ASK_DOCS_SERVER_BASIC_AUTH_PASSWORD)
        self.headers = {
            "Authorization": self.auth_header,
            "X-Request-ID": request_id_context.get(None)
        }

    @staticmethod
    def _create_auth_header(username: str, password: str) -> str:
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded_credentials}"

    async def ask(self, request: str) -> AnswerResponse:
        try:
            async with ClientSession() as session:
                async with session.post(
                        url=f"{self.base_url}/docs/ask",
                        headers=self.headers,
                        json={'question': request},
                        ssl=False
                ) as response:
                    logger.info(f"Got answer from ask-docs backend service")
                    json_response = await response.json()
                    logger.debug(f"Response: {json_response}")
                    return AnswerResponse(**json_response)
        except Exception as e:
            logger.error(f"Failed to get answer from ask-docs backend service: {e}")
            raise

    async def health_check(self) -> Dict[str, str]:
        try:
            async with ClientSession() as session:
                async with session.get(
                        url=self.health_check_url,
                        ssl=False
                ) as response:
                    logger.info(f"Health check passed for ask-docs backend service")
                    return response.json()
        except Exception as e:
            logger.error(f"Failed to check health for ask-docs backend service: {e}")
            return {"status": "unhealthy"}
