from typing import List, Optional
from pydantic import BaseModel, Field, validator


class SegmentRevenue(BaseModel):
    name: str
    revenue: Optional[float] = Field(default=None, ge=0)

    @validator("name")
    def name_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Segment name must not be empty")
        return value.strip()


class ExtractionResult(BaseModel):
    company: str = Field(default="Apple")
    document_name: Optional[str] = None
    reporting_period: Optional[str] = None
    currency: str = Field(default="USD")

    revenue_total: Optional[float] = Field(default=None, ge=0)
    net_income: Optional[float] = Field(default=None, ge=0)
    operating_income: Optional[float] = Field(default=None, ge=0)
    rnd_expense: Optional[float] = Field(default=None, ge=0)
    services_revenue: Optional[float] = Field(default=None, ge=0)

    segments: List[SegmentRevenue] = Field(default_factory=list)

    # for explainability / debugging
    source_chunks: List[str] = Field(default_factory=list)

    # notes from extraction process
    notes: List[str] = Field(default_factory=list)

    @validator("company")
    def normalize_company(cls, value: str) -> str:
        return value.strip()

    @validator("currency")
    def normalize_currency(cls, value: str) -> str:
        return value.upper().strip()