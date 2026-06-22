from pydantic import BaseModel


class LoanCloseResponse(BaseModel):

    loan_account_id: int

    loan_status: str

    message: str