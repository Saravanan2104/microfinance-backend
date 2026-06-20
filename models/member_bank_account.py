from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean
)

from sqlalchemy.orm import relationship

from database.base import Base


class MemberBankAccount(Base):
    __tablename__ = "member_bank_accounts"

    bank_account_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    member_id = Column(
        Integer,
        ForeignKey("members.member_id"),
        nullable=False
    )

    account_holder_name = Column(
        String(255),
        nullable=False
    )

    account_number = Column(
        String(50),
        nullable=False
    )

    ifsc_code = Column(
        String(20),
        nullable=False
    )

    bank_name = Column(
        String(255),
        nullable=False
    )

    branch_name = Column(
        String(255)
    )

    is_primary = Column(
        Boolean,
        default=True
    )

    member = relationship(
        "Member",
        backref="bank_accounts"
    )