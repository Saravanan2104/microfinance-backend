from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from services.report_service import (
    ReportService
)

from schemas.report_schema import (
    CollectionReportResponse,
    LoanReportResponse,
    OverdueReportResponse
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/collections",
    response_model=CollectionReportResponse
)
def get_collection_report(
    db: Session = Depends(get_db)
):

    return (
        ReportService
        .get_collection_report(db)
    )


@router.get(
    "/loans",
    response_model=LoanReportResponse
)
def get_loan_report(
    db: Session = Depends(get_db)
):

    return (
        ReportService
        .get_loan_report(db)
    )


@router.get(
    "/overdues",
    response_model=OverdueReportResponse
)
def get_overdue_report(
    db: Session = Depends(get_db)
):

    return (
        ReportService
        .get_overdue_report(db)
    )