# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

import os
import tempfile

from fastapi import APIRouter, UploadFile, File
from fastapi import Depends

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
    - file (UploadFile): The file to load.

    Returns:
    - str: A message indicating the success of loading and indexing the document chunks.

    """
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file_path = temp_file.name
    try:
        documents = await loader_srv.load_from_documents(file_type, temp_file_path)
        await vector_srv.add_items(documents)
        return {"message": f"Successfully loaded and indexed {len(documents)} document chunks"}
    finally:
        os.unlink(temp_file_path)
