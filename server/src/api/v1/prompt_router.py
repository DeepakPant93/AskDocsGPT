# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

from http import HTTPStatus

from fastapi import APIRouter

from ...core.logger import logger
from ...schema.v1.schema import PromptOutputSchema, PromptInputSchema

router = APIRouter()


@router.post("/invoke", status_code=HTTPStatus.OK, response_model=PromptOutputSchema)
async def invoke(request: PromptInputSchema) -> PromptOutputSchema:
    """
    Invoke the GPT model with a given prompt.

    Args:
    request (PromptInputSchema): The input to the GPT model, containing the prompt.

    Returns:
    PromptOutputSchema: The output of the GPT model, containing the response.
    """

    logger.info("Invoking GPT model with prompt: %s", request.question)
    return PromptOutputSchema(answer="Hello World:: " + request.question)
