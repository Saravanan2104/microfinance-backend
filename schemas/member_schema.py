from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

class MemberCreate(BaseModel):
    group_id: int
    first_name: str
    last_name: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    phone: str    
    secondary_number: Optional[str] = None 
   


class MemberUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    phone: Optional[str] = None    
    secondary_number: Optional[str] = None

    


class MemberResponse(BaseModel):
    member_id: int
    member_code: str
    first_name: str
    last_name: Optional[str]
    dob: Optional[date]
    gender: Optional[str]
    marital_status: Optional[str]
    phone: str    
    secondary_number: Optional[str]

    

    class Config:
        from_attributes = True