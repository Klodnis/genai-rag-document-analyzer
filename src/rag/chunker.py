from typing import List

class TextChunker:
    """
    Splits text into overlapping word-based chunks.
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[str]:
        words = text.split()
        chunks: List[str] = []

        start = 0
        while start < len(words):
            end = start + self.chunk_size
            chunk_words = words[start:end]
            chunks.append(" ".join(chunk_words))
            start = end - self.overlap

        return chunks