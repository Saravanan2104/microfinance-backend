from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.role import Role
from schemas.role_schema import RoleCreate

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post("")
def create_role(
    payload: RoleCreate,
    db: Session = Depends(get_db)
):

    role = Role(
        role_name=payload.role_name
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role

@router.get("")
def get_roles(
    db: Session = Depends(get_db)
):
    return db.query(Role).all()