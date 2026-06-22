from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.loan_schema import (
    LoanApplicationCreate,
    LoanApplicationUpdate,
    LoanApplicationResponse,
    LoanApprovalRequest
)

from services.loan_service import LoanService


router = APIRouter(
    prefix="/loan-applications",
    tags=["Loan Applications"]
)


@router.post(
    "",
    response_model=LoanApplicationResponse
)
def create_loan_application(
    payload: LoanApplicationCreate,
    db: Session = Depends(get_db)
):

    return LoanService.create_loan_application(
        db=db,
        data=payload
    )


@router.get(
    "",
    response_model=list[LoanApplicationResponse]
)
def get_loan_applications(
    db: Session = Depends(get_db)
):

    return LoanService.get_all_loan_applications(
        db
    )


@router.get(
    "/{loan_application_id}",
    response_model=LoanApplicationResponse
)
def get_loan_application(
    loan_application_id: int,
    db: Session = Depends(get_db)
):

    loan_application = (
        LoanService.get_loan_application_by_id(
            db,
            loan_application_id
        )
    )

    if not loan_application:
        raise HTTPException(
            status_code=404,
            detail="Loan application not found"
        )

    return loan_application


@router.put(
    "/{loan_application_id}",
    response_model=LoanApplicationResponse
)
def update_loan_application(
    loan_application_id: int,
    payload: LoanApplicationUpdate,
    db: Session = Depends(get_db)
):

    loan_application = (
        LoanService.get_loan_application_by_id(
            db,
            loan_application_id
        )
    )

    if not loan_application:
        raise HTTPException(
            status_code=404,
            detail="Loan application not found"
        )

    return LoanService.update_loan_application(
        db,
        loan_application,
        payload
    )


@router.post(
    "/{loan_application_id}/submit",
    response_model=LoanApplicationResponse
)
def submit_application(
    loan_application_id: int,
    db: Session = Depends(get_db)
):

    loan_application = (
        LoanService.get_loan_application_by_id(
            db,
            loan_application_id
        )
    )

    if not loan_application:
        raise HTTPException(
            status_code=404,
            detail="Loan application not found"
        )

    return LoanService.submit_application(
        db,
        loan_application
    )


@router.post(
    "/{loan_application_id}/rm-approve",
    response_model=LoanApplicationResponse
)
def rm_approve(
    loan_application_id: int,
    payload: LoanApprovalRequest,
    db: Session = Depends(get_db)
):

    loan_application = (
        LoanService.get_loan_application_by_id(
            db,
            loan_application_id
        )
    )

    if not loan_application:
        raise HTTPException(
            status_code=404,
            detail="Loan application not found"
        )

    return LoanService.rm_approve(
        db,
        loan_application,
        payload
    )


@router.post(
    "/{loan_application_id}/bm-approve",
    response_model=LoanApplicationResponse
)
def bm_approve(
    loan_application_id: int,
    payload: LoanApprovalRequest,
    db: Session = Depends(get_db)
):

    loan_application = (
        LoanService.get_loan_application_by_id(
            db,
            loan_application_id
        )
    )

    if not loan_application:
        raise HTTPException(
            status_code=404,
            detail="Loan application not found"
        )

    return LoanService.bm_approve(
        db,
        loan_application,
        payload
    )


@router.post(
    "/{loan_application_id}/admin-approve",
    response_model=LoanApplicationResponse
)
def admin_approve(
    loan_application_id: int,
    payload: LoanApprovalRequest,
    db: Session = Depends(get_db)
):

    loan_application = (
        LoanService.get_loan_application_by_id(
            db,
            loan_application_id
        )
    )

    if not loan_application:
        raise HTTPException(
            status_code=404,
            detail="Loan application not found"
        )

    return LoanService.admin_approve(
        db,
        loan_application,
        payload
    )

@router.get(
    "/member/{member_id}",
    response_model=list[LoanApplicationResponse]
)
def get_member_loans(
    member_id: int,
    db: Session = Depends(get_db)
):

    return LoanService.get_member_loans(
        db,
        member_id
    )

@router.post(
    "/loan-account/{loan_account_id}/close"
)
def close_loan(
    loan_account_id: int,
    db: Session = Depends(get_db)
):

    return (
        LoanService.close_loan(
            db,
            loan_account_id
        )
    )