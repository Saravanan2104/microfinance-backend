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


class LoanAccount(Base):
    __tablename__ = "loan_accounts"

    loan_account_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    loan_application_id = Column(
        Integer,
        ForeignKey("loan_applications.loan_application_id"),
        nullable=False
    )

    loan_account_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    sanctioned_amount = Column(
        Float,
        nullable=False
    )

    interest_rate = Column(
        Float,
        nullable=False
    )

    tenure_months = Column(
        Integer,
        nullable=False
    )

    emi_amount = Column(
        Float,
        nullable=False
    )

    sanctioned_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    loan_status = Column(
        String(50),
        default="ACTIVE"
    )

    loan_application = relationship(
        "LoanApplication"
    )