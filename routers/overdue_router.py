from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from services.overdue_service import (
    OverdueService
)

from schemas.repayment_schema import (
    RepaymentScheduleResponse
)


router = APIRouter(
    prefix="/overdues",
    tags=["Overdues"]
)


@router.get(
    "",
    response_model=list[
        RepaymentScheduleResponse
    ]
)
def get_overdues(
    db: Session = Depends(get_db)
):

    return (
        OverdueService
        .get_overdue_installments(
            db
        )
    )