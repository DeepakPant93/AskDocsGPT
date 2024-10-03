# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

class Document:
    page_content: str
    metadata: dict = {}


class QuestionRequest:
    question: str


class AnswerResponse:
    def __init__(self, answer: str, source_documents: list[Document]):
        self.answer = answer
        self.source_documents = source_documents
