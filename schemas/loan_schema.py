from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class LoanApplicationCreate(BaseModel):
    application_number: str

    member_id: int
    group_id: int

    requested_amount: float

    loan_purpose: Optional[str] = None

    created_by: int


class LoanApplicationUpdate(BaseModel):
    requested_amount: Optional[float] = None

    loan_purpose: Optional[str] = None


class LoanApplicationResponse(BaseModel):
    loan_application_id: int

    application_number: str

    member_id: int
    group_id: int

    requested_amount: float

    loan_purpose: Optional[str]

    application_status: str

    applied_date: datetime

    created_by: Optional[int]

    class Config:
        from_attributes = True


class LoanApplicationSubmitRequest(BaseModel):
    remarks: Optional[str] = None


class LoanApprovalRequest(BaseModel):
    employee_id: int

    remarks: Optional[str] = None


class LoanRejectionRequest(BaseModel):
    employee_id: int

    remarks: str