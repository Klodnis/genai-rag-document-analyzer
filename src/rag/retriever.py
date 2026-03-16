from typing import List

from rag.chunker import TextChunker
from rag.embeddings import EmbeddingService
from rag.vector_store import VectorStore


class DocumentRetriever:
    """
    High-level interface for semantic document retrieval.
    """

    def __init__(self):
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.vector_store: VectorStore | None = None

    def index_documents(self, documents: List[str]) -> None:
        all_chunks: List[str] = []

        for doc in documents:
            chunks = self.chunker.chunk(doc)
            all_chunks.extend(chunks)

        embeddings = self.embedding_service.embed(all_chunks)
        embedding_dim = embeddings.shape[1]

        self.vector_store = VectorStore(embedding_dim)
        self.vector_store.add(embeddings, all_chunks)

    def search(self, query: str, top_k: int = 5):
        if not self.vector_store:
            raise RuntimeError("Documents have not been indexed yet")

        query_embedding = self.embedding_service.embed([query])
        return self.vector_store.search(query_embedding, top_k)