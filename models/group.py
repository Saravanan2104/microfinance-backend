from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float
)

from sqlalchemy.orm import relationship

from database.base import Base


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    group_code = Column(
        String(50),
        unique=True,
        nullable=False
    )

    group_name = Column(
        String(255),
        nullable=False
    )

    branch_id = Column(
        Integer,
        ForeignKey("branches.branch_id"),
        nullable=False
    )

    location_id = Column(
        Integer,
        ForeignKey("locations.location_id"),
        nullable=False
    )

    
    head_member_id = Column(
        Integer,
        ForeignKey("members.member_id")
    )

    sub_head_member_id = Column(
        Integer,
        ForeignKey("members.member_id")
    )

    group_limit_amount = Column(
        Float,
        default=0
    )

    status = Column(
        String(20),
        default="ACTIVE"
    )

    branch = relationship("Branch")
    location = relationship("Location")
    

    head_member = relationship(
        "Member",
        foreign_keys=[head_member_id]
    )

    sub_head_member = relationship(
        "Member",
        foreign_keys=[sub_head_member_id]
    )