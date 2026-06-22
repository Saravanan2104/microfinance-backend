from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from services.dashboard_service import (
    DashboardService
)

from schemas.dashboard_schema import (
    DashboardResponse
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "",
    response_model=DashboardResponse
)
def get_dashboard(
    db: Session = Depends(get_db)
):

    return (
        DashboardService
        .get_dashboard(db)
    )