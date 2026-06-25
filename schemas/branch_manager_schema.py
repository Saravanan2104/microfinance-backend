from pydantic import BaseModel, EmailStr


class BranchManagerCreate(BaseModel):

    password: str

    first_name: str

    last_name: str

    email: EmailStr

    phone: str