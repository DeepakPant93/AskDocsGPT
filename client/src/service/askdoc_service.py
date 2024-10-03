# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

from ..proxies.askdocs_proxy import AskDocsAPIProxy
from ..schema.v1.prompt_schema import AnswerResponse


class AskDocsService:
    def __init__(self):
        self.docs_proxy = AskDocsAPIProxy()

    async def ask(self, request: str) -> AnswerResponse:
        try:
            return await self.docs_proxy.ask(request)
        except Exception:
            return "Failed to get answer from ask-docs backend service. Please try again later."

    async def health_check(self) -> bool:
        res: dict = await self.docs_proxy.health_check()
        return True if res.get('status') == 'healthy' else False
