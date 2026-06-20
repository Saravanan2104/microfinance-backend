from fastapi import HTTPException

from models.member import Member


class AuthService:

    @staticmethod
    def member_login(
        db,
        member_code,
        password
    ):

        member = (
            db.query(Member)
            .filter(
                Member.member_code == member_code
            )
            .first()
        )

        if not member:
            raise HTTPException(
                status_code=401,
                detail="Invalid member code or password"
            )

        if member.password_hash != password:
            raise HTTPException(
                status_code=401,
                detail="Invalid member code or password"
            )

        if not member.is_active:
            raise HTTPException(
                status_code=403,
                detail="Member account is inactive"
            )

        return {
            "message": "Login successful",
            "member_code": member.member_code,
            "member_name": member.first_name
        }