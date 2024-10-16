import unittest
from unittest.mock import create_autospec, AsyncMock, Mock

from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
from langchain.llms import OpenAI
from langchain_core.documents import Document

from ...src.schema.v1.schema import AnswerResponse
from ...src.service.qa_service import QAService
from ...src.service.vector_store_service import VectorStoreService


class TestQAService(
    unittest.IsolatedAsyncioTestCase):  # IsolatedAsyncioTestCase:: writing for async test cases

    def setUp(self):
        # Arrange
        self.mock_qa_srv: QAService = QAService(vector_srv=create_autospec(VectorStoreService))
        self.mock_qa_srv.llm = create_autospec(OpenAI)
        self.mock_qa_srv.chain = create_autospec(BaseCombineDocumentsChain)

    def tearDown(self):
        pass

    async def test_ask_with_relevant_query(self):
        # Mock
        self.mock_qa_srv.vector_srv.get_similar_documents = AsyncMock(return_value=[
            Document(page_content="The capital of France is Paris.", metadata={"source": "https://example.com"}),
            Document(page_content="The capital of India is New Delhi.", metadata={"source": "https://example.com"})
        ])
        self.mock_qa_srv.chain.run = Mock(return_value="The capital of France is Paris.")

        query = "What is the capital of France?"

        # Act
        res: AnswerResponse = await self.mock_qa_srv.ask(query)

        # Assert
        self.assertEqual(res.answer, "The capital of France is Paris.")
        self.assertEqual(len(res.source_documents), 2)

    async def test_ask_with_irrelevant_query(self):
        # Mock
        self.mock_qa_srv.vector_srv.get_similar_documents = AsyncMock(return_value=[])
        self.mock_qa_srv.chain.run = Mock(return_value=self.mock_qa_srv.NEGATIVE_RESPONSE_MSG)

        query = "What is the capital of South Korea?"

        # Act
        res: AnswerResponse = await self.mock_qa_srv.ask(query)

        # Assert
        self.assertEqual(res.answer, self.mock_qa_srv.NEGATIVE_RESPONSE_MSG)
        self.assertEqual(res.source_documents, None)


if __name__ == '__main__':
    unittest.main()
