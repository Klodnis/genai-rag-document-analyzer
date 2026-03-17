from typing import List, Dict

from sentence_transformers import CrossEncoder


class Reranker:
    """
    Cross-encoder based reranker for improving retrieval precision.
    """

    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        candidates: List[Dict],
        top_k: int = 5,
    ) -> List[Dict]:
        """
        Rerank retrieved text chunks using a cross-encoder.

        candidates: List of dicts with at least {"text": "..."}
        """
        pairs = [(query, c["text"]) for c in candidates]

        scores = self.model.predict(pairs)

        for candidate, score in zip(candidates, scores):
            candidate["rerank_score"] = float(score)

        candidates.sort(key=lambda x: x["rerank_score"], reverse=True)

        return candidates[:top_k]