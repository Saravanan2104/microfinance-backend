from pydantic import BaseModel, EmailStr


class BranchManagerCreate(BaseModel):

    password: str

    first_name: str

    last_name: str

    email: EmailStr

    phone: str


class BranchManagerResponse(BaseModel):

    employee_id: int

    employee_code: str

    username: str

    first_name: str

    last_name: str

    email: str

    phone: str

    class Config:
        from_attributes = True