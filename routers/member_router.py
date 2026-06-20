from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.member_schema import (
    MemberCreate,
    MemberUpdate,
    MemberResponse
)

from services.member_service import MemberService


router = APIRouter(
    prefix="/members",
    tags=["Members"]
)


@router.post(
    "",
    response_model=MemberResponse
)
def create_member(
    payload: MemberCreate,
    db: Session = Depends(get_db)
):

    return MemberService.create_member(
        db=db,
        data=payload
    )


@router.get(
    "",
    response_model=list[MemberResponse]
)
def get_members(
    db: Session = Depends(get_db)
):

    return MemberService.get_all_members(
        db
    )


@router.get(
    "/{member_id}",
    response_model=MemberResponse
)
def get_member(
    member_id: int,
    db: Session = Depends(get_db)
):

    member = (
        MemberService.get_member_by_id(
            db,
            member_id
        )
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return member


@router.put(
    "/{member_id}",
    response_model=MemberResponse
)
def update_member(
    member_id: int,
    payload: MemberUpdate,
    db: Session = Depends(get_db)
):

    member = (
        MemberService.get_member_by_id(
            db,
            member_id
        )
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return MemberService.update_member(
        db,
        member,
        payload
    )