from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from core.permissions import admin_only

from schemas.branch_manager_schema import (
    BranchManagerCreate
)

from services.branch_manager_service import (
    BranchManagerService
)

router = APIRouter(
    prefix="/branch-managers",
    tags=["Branch Managers"]
)


@router.post("")
def create_branch_manager(
    payload: BranchManagerCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):

    return BranchManagerService.create_branch_manager(
        db=db,
        data=payload
    )