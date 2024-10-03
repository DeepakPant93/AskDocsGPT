# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

from fastapi.params import Depends
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

from .vector_store_service import VectorStoreService
from ..core.config import settings
from ..core.logger import logger
# from ..repository.vector_store import VectorStoreRepository
from ..schema.v1.schema import AnswerResponse, Document


class QAService:
    def __init__(self, vector_srv: VectorStoreService = Depends()):
        self.llm = OpenAI(model_name=settings.MODEL_NAME, openai_api_key=settings.OPENAI_API_KEY)
        self.chain = load_qa_chain(self.llm, chain_type="stuff")
        self.vector_srv = vector_srv

    def ask(self, question: str):
        logger.info("Asking question: %s", question)
        similar_documents = self.vector_srv.get_similar_documents(question)
        answer = self.chain.run(input_documents=similar_documents, question=question)
        source_docs = [Document(page_content=docs.page_content, metadata=docs.metadata) for docs in
                       similar_documents]
        return AnswerResponse(answer=answer, source_documents=source_docs)
