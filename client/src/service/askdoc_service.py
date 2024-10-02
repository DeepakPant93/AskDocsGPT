# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

from typing import Any, Dict

from ..proxies.askdocs_proxy import AskDocsAPIProxy
from ..schema.v1.prompt_schema import PromptOutputSchema


class AskDocsService:
    def __init__(self):
        self.docs_proxy = AskDocsAPIProxy()

    async def invoke(self, request: str) -> Dict[str, Any]:
        try:
            res: PromptOutputSchema = await self.docs_proxy.invoke(request)
            return res.answer
        except Exception:
            return "Failed to get answer from ask-docs backend service. Please try again later."

    async def health_check(self) -> bool:
        res: dict = await self.docs_proxy.health_check()
        return True if res.get('status') == 'healthy' else False
