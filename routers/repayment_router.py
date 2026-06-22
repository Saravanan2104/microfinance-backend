from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from services.repayment_service import (
    RepaymentService
)

from schemas.repayment_schema import (
    RepaymentScheduleResponse
)


router = APIRouter(
    prefix="/repayments",
    tags=["Repayments"]
)


@router.get(
    "/loan-account/{loan_account_id}",
    response_model=list[
        RepaymentScheduleResponse
    ]
)
def get_schedule(
    loan_account_id: int,
    db: Session = Depends(get_db)
):

    return (
        RepaymentService
        .get_schedule_by_loan_account(
            db,
            loan_account_id
        )
    )