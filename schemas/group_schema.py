from typing import Optional

from pydantic import BaseModel


class GroupCreate(BaseModel):
    group_code: str
    group_name: str

    branch_id: int
    location_id: int

    

    group_limit_amount: float


class GroupUpdate(BaseModel):
    group_name: Optional[str] = None

    branch_id: Optional[int] = None
    location_id: Optional[int] = None

    

    group_limit_amount: Optional[float] = None

    status: Optional[str] = None


class GroupResponse(BaseModel):
    group_id: int

    group_code: str
    group_name: str

    branch_id: int
    location_id: int

    relationship_manager_employee_id: int

    head_member_id: Optional[int]
    sub_head_member_id: Optional[int]

    group_limit_amount: float

    status: str

    class Config:
        from_attributes = True


class AddMembersToGroupRequest(BaseModel):
    member_ids: list[int]




class AssignHeadRequest(BaseModel):
    member_id: int

    changed_by_employee_id: int

    remarks: Optional[str] = None



class AssignSubHeadRequest(BaseModel):
    member_id: int

    changed_by_employee_id: int

    remarks: Optional[str] = None


class GroupMemberResponse(BaseModel):
    group_member_id: int

    group_id: int

    member_id: int

    status: str

    class Config:
        from_attributes = True