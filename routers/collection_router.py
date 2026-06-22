from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.collection_schema import (
    CollectionCreate,
    CollectionResponse
)

from services.collection_service import (
    CollectionService
)


router = APIRouter(
    prefix="/collections",
    tags=["Collections"]
)


@router.post(
    "",
    response_model=CollectionResponse
)
def create_collection(
    payload: CollectionCreate,
    db: Session = Depends(get_db)
):

    return (
        CollectionService.create_collection(
            db,
            payload
        )
    )


@router.get(
    "/loan-account/{loan_account_id}",
    response_model=list[
        CollectionResponse
    ]
)
def get_collections(
    loan_account_id: int,
    db: Session = Depends(get_db)
):

    return (
        CollectionService
        .get_collections_by_loan_account(
            db,
            loan_account_id
        )
    )