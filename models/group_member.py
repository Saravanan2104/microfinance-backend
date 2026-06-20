from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    String
)

from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class GroupMember(Base):
    __tablename__ = "group_members"

    group_member_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    group_id = Column(
        Integer,
        ForeignKey("groups.group_id"),
        nullable=False
    )

    member_id = Column(
        Integer,
        ForeignKey("members.member_id"),
        nullable=False,
        unique=True
    )

    joined_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    removed_at = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String(20),
        default="ACTIVE"
    )

    group = relationship(
        "Group",
        backref="group_members"
    )

    member = relationship(
        "Member",
        backref="group_members"
    )