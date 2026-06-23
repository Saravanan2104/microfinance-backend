from pydantic import BaseModel


class CollectionReportResponse(BaseModel):
    total_collections: float
    total_transactions: int


class LoanReportResponse(BaseModel):
    total_loans: int
    active_loans: int
    closed_loans: int


class OverdueReportResponse(BaseModel):
    overdue_installments: int
    overdue_amount: float