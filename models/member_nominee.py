from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database.base import Base


class MemberNominee(Base):
    __tablename__ = "member_nominees"

    nominee_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    member_id = Column(
        Integer,
        ForeignKey("members.member_id"),
        nullable=False
    )

    nominee_name = Column(
        String(255),
        nullable=False
    )

    relationship_type = Column(
        String(100),
        nullable=False
    )

    phone_number = Column(
        String(20),
        nullable=False
    )

    member = relationship(
        "Member",
        backref="nominees"
    )