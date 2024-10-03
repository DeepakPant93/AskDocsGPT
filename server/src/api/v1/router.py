# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

import os
import tempfile
from http import HTTPStatus

from fastapi import APIRouter, UploadFile, File
from fastapi import Depends

from ...core.config import settings
from ...core.exception import ADException
from ...schema.v1.schema import AnswerResponse, QuestionRequest, FileType
from ...service.document_loader import DocumentLoaderService
from ...service.qa_service import QAService
from ...service.vector_store_service import VectorStoreService

router = APIRouter()


@router.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest, service: QAService = Depends()):
    """
    Post a question to the QA service to retrieve an answer.

    Args:
    - request (QuestionRequest): The user's question.

    Returns:
    - AnswerResponse: A response containing the answer from the QA service.

    """
    return await service.ask(request.question)


@router.post("/load")
async def load(file_type: FileType, file: UploadFile = File(...),
               loader_srv: DocumentLoaderService = Depends(),
               vector_srv: VectorStoreService = Depends()):
    """
    Load a file into the vector store.

    Args:
    - file_type (FileType): The type of file to load. Supported file types: PDF
    - file (UploadFile): The file to load. Max file size: 10 MB

    Returns:
    - str: A message indicating the success of loading and indexing the document chunks.

    """
    original_name = file.filename
    # file_size = await file.seek(0)  # Get the file size
    # await file.seek(0)  # Reset file pointer to the beginning
    #
    # # Check if the file size exceeds 10 MB (10 * 1024 * 1024 bytes)
    # if file_size > settings.MAX_FILE_SIZE:
    #     raise ADException(status_code=HTTPStatus.BAD_REQUEST,
    #                       detail="File size exceeds 10 MB. Please upload a smaller file.")

    # Create the temporary file with the original name in the system's temp directory
    temp_file_path = os.path.join(tempfile.gettempdir(), original_name)

    # Write the content to a temporary file with the original name
    with open(temp_file_path, 'wb') as temp_file:
        content = await file.read()
        temp_file.write(content)
    try:
        documents = await loader_srv.load_from_documents(file_type, temp_file_path)
        await vector_srv.add_items(documents)
        return {"message": f"Successfully loaded and indexed {len(documents)} document chunks"}
    finally:
        os.unlink(temp_file_path)
