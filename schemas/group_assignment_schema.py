from pydantic import BaseModel
from datetime import date


class GroupAssignmentCreate(
    BaseModel
):
    group_id: int
    rm_employee_id: int
    qa_employee_id: int


class GroupAssignmentResponse(
    BaseModel
):
    group_assignment_id: int
    group_id: int
    rm_employee_id: int
    qa_employee_id: int
    assigned_date: date

    model_config = {
        "from_attributes": True
    }