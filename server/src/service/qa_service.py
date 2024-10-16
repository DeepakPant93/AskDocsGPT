# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

from fastapi.params import Depends
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

from .vector_store_service import VectorStoreService
from ..core.config import settings
from ..core.logger import logger
from ..schema.v1.schema import AnswerResponse, Document


class QAService:
    def __init__(self, vector_srv: VectorStoreService = Depends()):
        self.llm = OpenAI(model_name=settings.MODEL_NAME, openai_api_key=settings.OPENAI_API_KEY,
                          temperature=settings.TEMPERATURE, max_tokens=settings.MAX_TOKENS)
        self.chain = load_qa_chain(self.llm)
        self.vector_srv = vector_srv

    NEGATIVE_RESPONSE_MSG = "I don't know. Please ask a question related to the knowledge base, as I can only provide answers based on that information."

    async def ask(self, question: str) -> AnswerResponse:
        """
        Ask a question and get the answer with relevant source documents.

        Args:
        question (str): The question to ask

        Returns:
        AnswerResponse: The answer with relevant source documents
        """
        logger.info("Asking question: %s", question)

        # Define the prompt template to prevent the system from returning inappropriate or irrelevant answers
        prompt_template = """
                You are an expert assistant. Based on the following documents and question, provide only the answer without any additional explanations or information. 
                If the documents do not contain a relevant answer, respond with "{negative_response}".
                
                Documents:
                {documents}
                
                Question: {question}
                
                Answer:
        """

        # Get similar documents
        similar_documents = await self.vector_srv.get_similar_documents(question)

        # Format the prompt with the question and documents
        formatted_documents = "\n\n".join(
            [doc.page_content for doc in similar_documents])  # or doc.get('page_content') if dict

        prompt = prompt_template.format(documents=formatted_documents, question=question,
                                        negative_response=self.NEGATIVE_RESPONSE_MSG)

        answer = self.chain.run(input_documents=similar_documents, question=prompt)
        source_docs = None

        # Check if the answer is positive then get the source documents
        if answer.strip().lower() != self.NEGATIVE_RESPONSE_MSG.strip().lower():
            source_docs = [Document(page_content=docs.page_content, metadata=docs.metadata) for docs in
                           similar_documents]
        return AnswerResponse(answer=answer, source_documents=source_docs)
