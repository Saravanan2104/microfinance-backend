from pydantic import BaseModel


class MemberLoginRequest(BaseModel):
    member_code: str
    password: str


class LoginResponse(BaseModel):
    message: str
    member_code: str
    member_name: str