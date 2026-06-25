from datetime import date

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date,
    String
)

from database.base import Base


class BranchAssignment(Base):
    __tablename__ = "branch_assignments"

    branch_assignment_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    branch_id = Column(
        Integer,
        ForeignKey("branches.branch_id"),
        nullable=False
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    assigned_date = Column(
        Date,
        default=date.today
    )

    status = Column(
        String(20),
        default="ACTIVE"
    )