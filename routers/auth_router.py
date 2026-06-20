from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.auth_schema import (
    MemberLoginRequest,
    LoginResponse
)

from services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/member-login",
    response_model=LoginResponse
)
def member_login(
    payload: MemberLoginRequest,
    db: Session = Depends(get_db)
):

    return AuthService.member_login(
        db=db,
        member_code=payload.member_code,
        password=payload.password
    )