# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.
from uuid import uuid4

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from ..core.config import settings


class VectorStoreRepository:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.index = self.pc.Index(settings.PINECONE_INDEX_NAME)

    def add_items(self, documents):
        vector_store = PineconeVectorStore(index=self.index, embedding=self.embeddings)

        # Add documents to the vector store
        uuids = [str(uuid4()) for _ in range(len(documents))]  # Generate unique ids for each document
        vector_store.add_documents(documents=documents, ids=uuids)
        return uuids

    def get_similar_documents(self, query: str, k: int = 2):
        vector_store = PineconeVectorStore(index=self.index, embedding=self.embeddings)
        return vector_store.similarity_search(query, k=k)
