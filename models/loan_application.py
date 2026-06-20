from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class LoanApplication(Base):
    __tablename__ = "loan_applications"

    loan_application_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    application_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    member_id = Column(
        Integer,
        ForeignKey("members.member_id"),
        nullable=False
    )

    group_id = Column(
        Integer,
        ForeignKey("groups.group_id"),
        nullable=False
    )

    requested_amount = Column(
        Float,
        nullable=False
    )

    loan_purpose = Column(
        String(500)
    )

    application_status = Column(
        String(50),
        default="DRAFT"
    )

    applied_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    created_by = Column(
        Integer,
        ForeignKey("employees.employee_id")
    )

    member = relationship("Member")
    group = relationship("Group")
    creator = relationship(
        "Employee",
        foreign_keys=[created_by]
    )