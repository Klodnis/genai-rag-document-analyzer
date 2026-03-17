# GenAI RAG Document Analyzer

## Overview
A Retrieval-Augmented Generation (RAG) based system that analyzes
financial PDF documents, extracts structured insights, and visualizes them.

## Key Features
- PDF document ingestion
- Two-stage RAG (dense retrieval with FAISS + cross-encoder reranking)
- Modular architecture for RAG, LLMs, and visualization
- Local-first, reproducible setup

## Dataset
Financial reports in PDF format:
https://investor.apple.com/investor-relations/default.aspx

## Architecture

The system follows a Retrieval-Augmented Generation (RAG) architecture:

1. **Ingestion**
   - Load PDF documents
   - Extract raw text

2. **Retrieval (Two-Stage RAG)**
   - Split documents into overlapping text chunks
   - Generate semantic embeddings using SentenceTransformers
   - Store embeddings in a FAISS vector store
   - Retrieve relevant text chunks via semantic similarity search (Stage 1)
   - Re-rank retrieved chunks using a cross-encoder model (Stage 2)

3. **Extraction (Planned)**
   - Use LLMs to extract structured data from retrieved text

4. **Visualization (Planned)**
   - Visualize extracted insights (charts, graphs)

## Current Status

- ✅ PDF ingestion and text extraction
- ✅ Semantic retrieval using embeddings and FAISS (RAG Stage 1)
- ✅ Reranking with cross-encoder (planned)
- ⏳ LLM-based structured extraction (planned)
- ⏳ Data visualization (planned)

## Project Structure

```text
src/
  ingestion/      # PDF loading and text extraction
  rag/            # Chunking, embeddings, vector store, retrieval
  extraction/     # Structured data extraction (planned)
  llm/            # LLM providers (planned)
  visualization/  # Charts and graphs (planned)
  app/            # Application/UI layer

tests/             # Unit and integration tests
data/              # Sample and local data (not committed)
```

## Setup
Instructions will be added.

## Limitations
Will be documented.

## Future Improvements
Will be documented.