from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class GroupRoleHistory(Base):
    __tablename__ = "group_role_history"

    group_role_history_id = Column(
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
        nullable=False
    )

    role_type = Column(
        String(20),
        nullable=False
    )

    start_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    end_date = Column(
        DateTime,
        nullable=True
    )

    changed_by_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    remarks = Column(
        String(500)
    )

    group = relationship("Group")

    member = relationship("Member")

    changed_by = relationship(
        "Employee",
        foreign_keys=[changed_by_employee_id]
    )