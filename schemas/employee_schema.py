from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class EmployeeRole(str, Enum):
    RM = "RM"
    QA = "QA"
    BM = "BM"


class EmployeeCreate(BaseModel):

    role_name: EmployeeRole

    password: str

    first_name: str

    last_name: Optional[str] = None

    email: EmailStr

    phone: str

  