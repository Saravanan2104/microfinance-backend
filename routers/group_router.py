from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.group_schema import (
    GroupCreate,
    GroupUpdate,
    GroupResponse,
    AddMembersToGroupRequest,
    AssignHeadRequest,
    AssignSubHeadRequest
)

from services.group_service import GroupService


router = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)


@router.post(
    "",
    response_model=GroupResponse
)
def create_group(
    payload: GroupCreate,
    db: Session = Depends(get_db)
):
    return GroupService.create_group(
        db=db,
        data=payload
    )


@router.get(
    "",
    response_model=list[GroupResponse]
)
def get_groups(
    db: Session = Depends(get_db)
):
    return GroupService.get_all_groups(
        db
    )


@router.get(
    "/{group_id}",
    response_model=GroupResponse
)
def get_group(
    group_id: int,
    db: Session = Depends(get_db)
):

    group = GroupService.get_group_by_id(
        db,
        group_id
    )

    if not group:
        raise HTTPException(
            status_code=404,
            detail="Group not found"
        )

    return group


@router.put(
    "/{group_id}",
    response_model=GroupResponse
)
def update_group(
    group_id: int,
    payload: GroupUpdate,
    db: Session = Depends(get_db)
):

    group = GroupService.get_group_by_id(
        db,
        group_id
    )

    if not group:
        raise HTTPException(
            status_code=404,
            detail="Group not found"
        )

    return GroupService.update_group(
        db,
        group,
        payload
    )


@router.post(
    "/{group_id}/members"
)
def add_member_to_group(
    group_id: int,
    payload: AddMembersToGroupRequest,
    db: Session = Depends(get_db)
):

    return GroupService.add_member_to_group(
        db=db,
        group_id=group_id,
        member_ids=payload.member_ids
    )


@router.post(
    "/{group_id}/assign-head",
    response_model=GroupResponse
)
def assign_head(
    group_id: int,
    payload: AssignHeadRequest,
    db: Session = Depends(get_db)
):

    return GroupService.assign_head(
        db=db,
        group_id=group_id,
        data=payload
    )


@router.post(
    "/{group_id}/assign-sub-head",
    response_model=GroupResponse
)
def assign_sub_head(
    group_id: int,
    payload: AssignSubHeadRequest,
    db: Session = Depends(get_db)
):

    return GroupService.assign_sub_head(
        db=db,
        group_id=group_id,
        data=payload
    )