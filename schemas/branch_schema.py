from pydantic import BaseModel


class BranchCreate(BaseModel):
    branch_name: str


class BranchUpdate(BaseModel):
    branch_name: str


class BranchResponse(BaseModel):
    branch_id: int
    branch_code: str
    branch_name: str
    is_active: bool

    class Config:
        from_attributes = True