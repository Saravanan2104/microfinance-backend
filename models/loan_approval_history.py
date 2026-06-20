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


class LoanApprovalHistory(Base):
    __tablename__ = "loan_approval_history"

    loan_approval_history_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    loan_application_id = Column(
        Integer,
        ForeignKey("loan_applications.loan_application_id"),
        nullable=False
    )

    approved_by_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    action_type = Column(
        String(50),
        nullable=False
    )

    remarks = Column(
        String(1000)
    )

    action_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    loan_application = relationship(
        "LoanApplication"
    )

    approved_by = relationship(
        "Employee"
    )