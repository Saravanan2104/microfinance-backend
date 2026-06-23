from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class EmployeeRole(str, Enum):
    ADMIN = "ADMIN"
    BM = "BM"
    RM = "RM"
    QA = "QA"


class EmployeeCreate(BaseModel):

    role_name: EmployeeRole

    password: str

    first_name: str

    last_name: Optional[str] = None

    email: EmailStr

    phone: str

    branch_id: Optional[int] = None

    location_id: Optional[int] = None