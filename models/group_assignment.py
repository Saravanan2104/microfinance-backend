from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date
)

from datetime import date

from database.base import Base


class GroupAssignment(Base):
    __tablename__ = "group_assignments"

    group_assignment_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    group_id = Column(
        Integer,
        ForeignKey("groups.group_id"),
        nullable=False
    )

    rm_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    qa_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    assigned_date = Column(
        Date,
        default=date.today
    )