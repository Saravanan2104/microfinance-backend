from datetime import date

from pydantic import BaseModel


class RepaymentScheduleResponse(BaseModel):
    repayment_schedule_id: int

    loan_account_id: int

    installment_no: int

    due_date: date

    principal_amount: float

    interest_amount: float

    total_amount: float

    paid_amount: float

    balance_amount: float

    status: str

    class Config:
        from_attributes = True