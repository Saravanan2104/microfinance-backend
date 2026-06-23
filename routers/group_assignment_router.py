from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import (
    get_db
)

from schemas.group_assignment_schema import (
    GroupAssignmentCreate,
    GroupAssignmentResponse
)

from services.group_assignment_service import (
    GroupAssignmentService
)

router = APIRouter(
    prefix="/group-assignments",
    tags=["Group Assignments"]
)


@router.post(
    "",
    response_model=
    GroupAssignmentResponse
)
def assign_group(
    payload:
    GroupAssignmentCreate,

    db: Session =
    Depends(get_db)
):

    return (
        GroupAssignmentService.assign_group(
            db,
            payload
        )
    )


@router.get(
    "",
    response_model=
    list[
        GroupAssignmentResponse
    ]
)
def get_all(
    db: Session =
    Depends(get_db)
):
    return (
        GroupAssignmentService.get_all(
            db
        )
    )