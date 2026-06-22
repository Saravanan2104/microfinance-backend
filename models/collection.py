from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Date,
    ForeignKey
)

from database.base import Base


class Collection(Base):
    __tablename__ = "collections"

    collection_id = Column(
        Integer,
        primary_key=True,
        index=True
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

    member_id = Column(
        Integer,
        ForeignKey("members.member_id"),
        nullable=False
    )

    collection_date = Column(
        Date,
        nullable=False
    )

    collected_amount = Column(
        Float,
        nullable=False
    )

    collection_mode = Column(
        String(50),
        nullable=False
    )

    receipt_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    remarks = Column(
        String(500)
    )

    collected_by_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )