# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from ..core.config import settings
from ..core.logger import logger
from ..schema.v1.schema import FileType


class DocumentLoaderService:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

    def load_from_directory(self, directory_path: str):
        loader = DirectoryLoader(directory_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        return self.text_splitter.split_documents(documents)

    def load_from_pdf(self, file_path: str):
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        return self.text_splitter.split_documents(documents)

    def load_from_documents(self, file_type: FileType, file_path: str):
        logger.info(f"Loading documents from {file_path}")
        if file_type == FileType.PDF:
            return self.load_from_pdf(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
