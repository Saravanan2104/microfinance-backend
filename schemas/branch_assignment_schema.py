from datetime import date

from pydantic import BaseModel


class BranchAssignmentCreate(BaseModel):
    branch_id: int
    employee_id: int


class BranchAssignmentResponse(BaseModel):
    branch_assignment_id: int
    branch_id: int
    employee_id: int
    assigned_date: date
    status: str

    class Config:
        from_attributes = True