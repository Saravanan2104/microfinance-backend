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


class CollectionTransaction(Base):
    __tablename__ = "collection_transactions"

    collection_transaction_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    collection_id = Column(
        Integer,
        ForeignKey("collections.collection_id"),
        nullable=False
    )

    member_id = Column(
        Integer,
        ForeignKey("members.member_id"),
        nullable=False
    )

    loan_account_id = Column(
        Integer,
        ForeignKey("loan_accounts.loan_account_id"),
        nullable=False
    )

    repayment_schedule_id = Column(
        Integer,
        ForeignKey(
            "repayment_schedules.repayment_schedule_id"
        ),
        nullable=False
    )

    amount_paid = Column(
        Float,
        nullable=False
    )

    payment_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    payment_mode = Column(
        String(50),
        nullable=False
    )

    reference_number = Column(
        String(255)
    )

    collection = relationship("Collection")
    member = relationship("Member")
    loan_account = relationship("LoanAccount")
    repayment_schedule = relationship(
        "RepaymentSchedule"
    )