from typing import List, Dict

import faiss
import numpy as np


class VectorStore:
    """
    FAISS-based in-memory vector store.
    """

    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.chunks: List[str] = []

    def add(self, embeddings: np.ndarray, chunks: List[str]) -> None:
        if len(embeddings) != len(chunks):
            raise ValueError("Embeddings and chunks must have same length")

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> List[Dict]:
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            results.append(
                {
                    "text": self.chunks[idx],
                    "score": float(dist),
                }
            )

        return results