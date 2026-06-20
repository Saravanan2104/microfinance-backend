from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from database.base import Base


class Branch(Base):
    __tablename__ = "branches"

    branch_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    branch_code = Column(
        String(50),
        unique=True,
        nullable=False
    )

    branch_name = Column(
        String(255),
        nullable=False
    )

    address = Column(
        String(500)
    )

    city = Column(
        String(100)
    )

    state = Column(
        String(100)
    )

    pincode = Column(
        String(20)
    )

    is_active = Column(
        Boolean,
        default=True
    )