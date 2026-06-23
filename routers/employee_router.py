from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.employee_schema import (
    EmployeeCreate
)

from services.employee_service import (
    EmployeeService
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("")
def create_employee(
    payload: EmployeeCreate,
    db: Session = Depends(get_db)
):

    return (
        EmployeeService.create_employee(
            db,
            payload
        )
    )