# GenAI RAG Document Analyzer

## Overview
A Retrieval-Augmented Generation (RAG) based system that analyzes
financial PDF documents, extracts structured insights, and visualizes them.

## Key Features
- PDF document ingestion
- Two-stage RAG (dense retrieval + reranking)
- Pluggable LLM strategy (open-source and OpenAI)
- Structured data extraction
- Data visualization (charts)
- Local-first, reproducible setup

## Dataset
Financial reports in PDF format:
https://www.kaggle.com/datasets/gauravduttakiit/financial-reports-pdf

## Architecture (High Level)
- LlamaIndex for document indexing and retrieval
- FAISS as local vector store
- Cross-Encoder reranking model
- Streamlit-based local UI

## Setup
Instructions will be added.

## Limitations
Will be documented.

## Future Improvements
Will be documented.