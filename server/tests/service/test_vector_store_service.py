import unittest
from unittest.mock import create_autospec, AsyncMock

from langchain_core.documents import Document

from ...src.repository.vector_store import VectorStoreRepository
from ...src.service.vector_store_service import VectorStoreService


class TestVectorStoreService(
    unittest.IsolatedAsyncioTestCase):  # IsolatedAsyncioTestCase:: writing for async test cases

    def setUp(self):
        # Arrange
        self.vector_store_srv: VectorStoreService = VectorStoreService(vector_store=create_autospec(VectorStoreRepository))

    def tearDown(self):
        pass

    async def test_add_items(self):
        # Mock
        self.vector_store_srv.vector_store.add_items = AsyncMock(
            return_value=["9c5b94b1-35ad-49bb-b118-8e8fc24abf80", "9c5b94b1-35ad-49bb-b118-8e8fc24abf81"])

        documents: list[Document] = [
            Document(page_content="Hello, world!", metadata={"source": "https://example.com"}),
            Document(page_content="Another document", metadata={"source": "https://example.com"})
        ]

        # Act
        res = await self.vector_store_srv.add_items(documents)

        # Assert
        self.assertEqual(len(res), 2)
        self.assertEqual(res, ["9c5b94b1-35ad-49bb-b118-8e8fc24abf80", "9c5b94b1-35ad-49bb-b118-8e8fc24abf81"])

    async def test_get_similar_documents(self):
        # Mock
        self.vector_store_srv.vector_store.get_similar_documents = AsyncMock(return_value=[
            Document(page_content="Hello, world!", metadata={"source": "https://example.com"}),
            Document(page_content="Another document", metadata={"source": "https://example.com"})
        ])

        query: str = "Hello, world!"

        # Act
        res = await self.vector_store_srv.get_similar_documents(query)

        # Assert
        self.assertEqual(len(res), 2)
        self.assertEqual(res, [
            Document(page_content="Hello, world!", metadata={"source": "https://example.com"}),
            Document(page_content="Another document", metadata={"source": "https://example.com"})
        ])

if __name__ == '__main__':
    unittest.main()
