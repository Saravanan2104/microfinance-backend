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


class RepaymentSchedule(Base):
    __tablename__ = "repayment_schedules"

    repayment_schedule_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    loan_account_id = Column(
        Integer,
        ForeignKey("loan_accounts.loan_account_id"),
        nullable=False
    )

    installment_number = Column(
        Integer,
        nullable=False
    )

    due_date = Column(
        DateTime,
        nullable=False
    )

    principal_amount = Column(
        Float,
        default=0
    )

    interest_amount = Column(
        Float,
        default=0
    )

    emi_amount = Column(
        Float,
        nullable=False
    )

    paid_amount = Column(
        Float,
        default=0
    )

    balance_amount = Column(
        Float,
        default=0
    )

    status = Column(
        String(20),
        default="PENDING"
    )

    loan_account = relationship(
        "LoanAccount"
    )