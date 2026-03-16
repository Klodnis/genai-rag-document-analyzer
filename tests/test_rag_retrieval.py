from rag.retriever import DocumentRetriever


def test_rag_retrieval_with_synthetic_text():
    documents = [
        "Apple Inc. filed a quarterly report for the period ending December 27, 2025.",
        "The company reported revenue growth driven by iPhone sales.",
        "Market risks include inflation and supply chain disruptions."
    ]

    retriever = DocumentRetriever()
    retriever.index_documents(documents)

    results = retriever.search("What period does the report cover?")

    assert isinstance(results, list)
    assert len(results) > 0