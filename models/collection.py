from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class Collection(Base):
    __tablename__ = "collections"

    collection_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    group_id = Column(
        Integer,
        ForeignKey("groups.group_id"),
        nullable=False
    )

    collected_by_member_id = Column(
        Integer,
        ForeignKey("members.member_id")
    )

    received_by_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id")
    )

    collection_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    total_collected_amount = Column(
        Float,
        default=0
    )

    remarks = Column(
        String(500)
    )

    group = relationship("Group")

    collector = relationship(
        "Member",
        foreign_keys=[collected_by_member_id]
    )

    receiver = relationship(
        "Employee",
        foreign_keys=[received_by_employee_id]
    )