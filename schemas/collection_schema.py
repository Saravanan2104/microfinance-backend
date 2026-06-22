from datetime import date

from pydantic import BaseModel


class CollectionCreate(BaseModel):

    loan_account_id: int

    repayment_schedule_id: int

    member_id: int

    collection_date: date

    collected_amount: float

    collection_mode: str

    remarks: str | None = None

    collected_by_employee_id: int


class CollectionResponse(BaseModel):

    collection_id: int

    loan_account_id: int

    repayment_schedule_id: int

    member_id: int

    collection_date: date

    collected_amount: float

    collection_mode: str

    receipt_number: str

    remarks: str | None

    collected_by_employee_id: int

    class Config:
        from_attributes = True