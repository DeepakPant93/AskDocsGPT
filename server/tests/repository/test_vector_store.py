import unittest
from unittest.mock import create_autospec, Mock

import pytest
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from ...src.repository.vector_store import VectorStoreRepository


class TestVectorStoreRepository(
    unittest.IsolatedAsyncioTestCase):  # IsolatedAsyncioTestCase:: writing for async test cases

    def setUp(self):
        # Arrange
        self.mock_vector_store_repo: VectorStoreRepository = VectorStoreRepository()
        self.mock_vector_store_repo.embeddings = create_autospec(OpenAIEmbeddings)
        self.mock_vector_store_repo.pc = create_autospec(Pinecone)
        self.mock_vector_store_repo.index = create_autospec(PineconeVectorStore)

    def tearDown(self):
        pass

    async def test_add_items(self):
        # Mock
        mock_vector_store = create_autospec(PineconeVectorStore)
        mock_vector_store.add_documents = Mock(return_value="9c5b94b1-35ad-49bb-b118-8e8fc24abf80")


        documents: list[Document] = [
            Document(page_content="Hello, world!", metadata={"source": "https://example.com"}),
            Document(page_content="Another document", metadata={"source": "https://example.com"})
        ]

        # Act
        res = await self.mock_vector_store_repo.add_items(documents)

        # Assert
        self.assertEqual(len(res), 2)

    @pytest.mark.skip
    async def test_get_similar_documents(self):
        # Mock
        mock_vector_store = create_autospec(PineconeVectorStore)
        mock_vector_store.similarity_search = Mock(return_value=[
            Document(page_content="Hello, world!", metadata={"source": "https://example.com"}),
            Document(page_content="Another document", metadata={"source": "https://example.com"})
        ])
        self.mock_vector_store_repo.index = mock_vector_store

        query: str = "Hello, world!"

        # Act
        res = await self.mock_vector_store_repo.get_similar_documents(query=query)

        # Assert
        self.assertEqual(len(res), 2)
        self.assertEqual(res, [
            Document(page_content="Hello, world!", metadata={"source": "https://example.com"}),
            Document(page_content="Another document", metadata={"source": "https://example.com"})
        ])


if __name__ == '__main__':
    unittest.main()
