from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import (
    get_db
)

from schemas.auth_schema import (
    LoginRequest
)

from services.auth_service import (
    AuthService
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    return AuthService.login(
        db,
        payload
    )