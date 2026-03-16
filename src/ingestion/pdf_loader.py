from pathlib import Path
from typing import List

from pypdf import PdfReader
from llama_index.core import Document


class PDFLoader:
    """
    Loads PDF documents from a directory and extracts raw text.
    """

    def __init__(self, pdf_dir: str):
        self.pdf_dir = Path(pdf_dir)

        if not self.pdf_dir.exists():
            raise ValueError(f"PDF directory does not exist: {pdf_dir}")

    def load(self) -> List[Document]:
        documents: List[Document] = []

        for pdf_file in self.pdf_dir.glob("*.pdf"):
            reader = PdfReader(pdf_file)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            if text.strip():
                documents.append(
                    Document(
                        text=text,
                        metadata={"source": pdf_file.name},
                    )
                )

        return documents