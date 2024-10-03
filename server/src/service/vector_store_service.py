# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


from fastapi import Depends

from ..core.logger import logger
from ..repository.vector_store import VectorStoreRepository


class VectorStoreService:
    def __init__(self, vector_store: VectorStoreRepository = Depends()):
        self.vector_store = vector_store

    async def add_items(self, documents):
        """
        Add items to the vector store.

        Args:
            documents (List[Document]): List of documents to add to the vector store.

        Returns:
            List[str]: List of IDs of the documents added to the vector store.
        """
        logger.info(f"Adding {len(documents)} documents to the vector store")
        return await self.vector_store.add_items(documents)

    async def get_similar_documents(self, query: str, k: int = 2):
        """
        Get the k most similar documents to the given query.

        Args:
            query (str): The query to search for similar documents.
            k (int, optional): The number of similar documents to return. Defaults to 2.

        Returns:
            List[Document]: List of the k most similar documents.
        """
        results = await self.vector_store.get_similar_documents(query, k)
        logger.info(f"Found {len(results)} similar documents")
        return results
