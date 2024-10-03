# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


from fastapi import Depends

from ..core.logger import logger
from ..repository.vector_store import VectorStoreRepository


class VectorStoreService:
    def __init__(self, vector_store: VectorStoreRepository = Depends()):
        self.vector_store = vector_store

    def add_items(self, documents):
        logger.info(f"Adding {len(documents)} documents to the vector store")
        return self.vector_store.add_items(documents)

    def get_similar_documents(self, query: str, k: int = 2):
        results = self.vector_store.get_similar_documents(query, k)
        logger.info(f"Found {len(results)} similar documents")
        return results
