from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session
from database.dependencies import get_db
from schemas.employee_schema import EmployeeCreate
from services.employee_service import EmployeeService
from core.auth import get_current_user
from core.permissions import admin_only

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("")
def create_employee(
    payload: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return (
        EmployeeService.create_employee(
            db,
            payload,
            current_user
        )
    )

@router.get("")
def get_all_employees(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return EmployeeService.get_all_employees(db)