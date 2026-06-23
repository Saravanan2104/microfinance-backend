from fastapi import HTTPException

from repositories.auth_repository import (
    AuthRepository
)

from core.security import (
    verify_password
)

from core.jwt_handler import (
    create_access_token
)


class AuthService:

    @staticmethod
    def login(
        db,
        data
    ):

        user = (
            AuthRepository
            .get_user_by_username(
                db,
                data.username
            )
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid username"
            )

        if not verify_password(
            data.password,
            user.password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid password"
            )

        token = (
            create_access_token(
                {
                    "sub":
                    user.username,

                    "role_id":
                    user.role_id
                }
            )
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }