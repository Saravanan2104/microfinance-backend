from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import (
    get_db
)

from schemas.branch_assignment_schema import (
    BranchAssignmentCreate,
    BranchAssignmentResponse
)

from services.branch_assignment_service import (
    BranchAssignmentService
)

router = APIRouter(
    prefix="/branch-assignments",
    tags=["Branch Assignments"]
)


@router.post(
    "",
    response_model=BranchAssignmentResponse
)
def assign_branch(
    payload: BranchAssignmentCreate,
    db: Session = Depends(get_db)
):

    return (
        BranchAssignmentService.assign_branch(
            db,
            payload
        )
    )