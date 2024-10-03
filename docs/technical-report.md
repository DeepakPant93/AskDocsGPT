# Technical Report: AskDocsGPT

## Overview

This solution implements a document-based question answering system using a microservices architecture, combining a
Streamlit frontend for user interaction and a FastAPI backend for document processing and answer generation. The system
leverages various technologies to enable efficient document indexing and intelligent question answering.

## Architecture Components

### Frontend (Streamlit)

- Provides an intuitive user interface for:
    - Document upload (currently PDF)
    - Question input
    - Answer display

### Backend (FastAPI)

- Handles document processing and question answering
- Implements RESTful endpoints for:
    - Document upload and processing
    - Question processing and answer generation

### Vector Database (Pinecone)

- Stores document embeddings for efficient similarity search
- Enables quick retrieval of relevant document chunks

### Key Technologies

1. **Document Processing**
    - LangChain Document Loaders
    - Text splitters for chunk generation
2. **Embedding Generation**
    - OpenAI Embeddings
3. **Vector Storage**
    - Pinecone vector database
4. **Question Answering**
    - OpenAI GPT-3.5 Turbo
    - LangChain QA Chain

## Process Flow

1. **Document Ingestion**
    - PDF upload
    - Text extraction and chunking
    - Embedding generation
    - Vector database storage

2. **Question Answering**
    - Question embedding generation
    - Similarity search in vector database
    - Context retrieval
    - Answer generation using GPT model

## Challenges and Solutions

1. **Challenge**: Matching dependencies
   **Solution**: Used `pip-compile` to manage dependencies and ensure compatibility

2. **Challenge**: Finding the required dependencies
   **Solution**: Used `pipreqs` to generate a list of dependencies required by the project

3. **Challenge**: Finding the right code according to the library version used
   **Solution**: Used `pipreqs` to generate a list of dependencies required by the project

4. **Challenge**: Answer generation quality and prevent the inappropriate answers
   **Solution**: Tried different prompts and fine-tuned the parameters to get the best results

5. **Challenge**: Vector database integration
   **Solution**: Used Pinecone for scalable and efficient vector storage

6. **Challenge**: Efficient document chunking
   **Solution**: Implemented RecursiveCharacterTextSplitter for optimal chunk size

## Future Enhancements

1. Support for additional document types
2. Improved chunking strategies
3. Enhanced error handling and recovery
4. User authentication and document management