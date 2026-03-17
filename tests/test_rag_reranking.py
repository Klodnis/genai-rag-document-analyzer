from rag.retriever import DocumentRetriever


def test_reranked_search_returns_results():
    documents = [
        "Apple Inc. filed a quarterly report for the period ending December 27, 2025.",
        "The company reported strong revenue growth.",
        "Market risks include inflation and supply chain disruptions."
    ]

    retriever = DocumentRetriever()
    retriever.index_documents(documents)

    results = retriever.search_with_rerank(
        "What period does the report cover?"
    )

    assert len(results) > 0
    assert "period" in results[0]["text"].lower()