from pathlib import Path

from ingestion.pdf_loader import PDFLoader


def test_pdf_loader_returns_documents():
    project_root = Path(__file__).resolve().parents[1]
    samples_dir = project_root / "data" / "samples"

    loader = PDFLoader(str(samples_dir))
    documents = loader.load()

    assert isinstance(documents, list)
    assert len(documents) > 0