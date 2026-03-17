import pytest
from extraction.schemas import ExtractionResult, SegmentRevenue


def test_extraction_result_valid():
    result = ExtractionResult(
        document_name="apple_2024.pdf",
        reporting_period="2024",
        revenue_total=1000.0,
        net_income=200.0,
        operating_income=300.0,
        segments=[
            SegmentRevenue(name="iPhone", revenue=500.0),
            SegmentRevenue(name="Mac", revenue=200.0),
        ],
    )

    assert result.company == "Apple"
    assert result.currency == "USD"
    assert len(result.segments) == 2


def test_negative_values_rejected():
    with pytest.raises(ValueError):
        ExtractionResult(revenue_total=-100.0)


def test_empty_segment_name_rejected():
    with pytest.raises(ValueError):
        SegmentRevenue(name="   ", revenue=100.0)


def test_optional_fields_allowed():
    result = ExtractionResult()

    assert result.revenue_total is None
    assert result.segments == []
    assert result.source_chunks == []


def test_currency_normalization():
    result = ExtractionResult(currency="usd")
    assert result.currency == "USD"