from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database.dependencies import (
    get_db
)

from schemas.branch_schema import (
    BranchCreate,
    BranchUpdate,
    BranchResponse
)

from services.branch_service import (
    BranchService
)

router = APIRouter(
    prefix="/branches",
    tags=["Branches"]
)


@router.post(
    "",
    response_model=BranchResponse
)
def create_branch(
    payload: BranchCreate,
    db: Session = Depends(get_db)
):

    return BranchService.create_branch(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[BranchResponse]
)
def get_all_branches(
    db: Session = Depends(get_db)
):

    return (
        BranchService.get_all_branches(
            db
        )
    )


@router.get(
    "/{branch_id}",
    response_model=BranchResponse
)
def get_branch(
    branch_id: int,
    db: Session = Depends(get_db)
):

    return (
        BranchService.get_branch_by_id(
            db,
            branch_id
        )
    )


@router.put(
    "/{branch_id}",
    response_model=BranchResponse
)
def update_branch(
    branch_id: int,
    payload: BranchUpdate,
    db: Session = Depends(get_db)
):

    branch = (
        BranchService.get_branch_by_id(
            db,
            branch_id
        )
    )

    return (
        BranchService.update_branch(
            db,
            branch,
            payload
        )
    )