from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean
)

from sqlalchemy.orm import relationship

from database.base import Base


class MemberIdentityProof(Base):
    __tablename__ = "member_identity_proofs"

    identity_proof_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    member_id = Column(
        Integer,
        ForeignKey("members.member_id"),
        nullable=False
    )

    aadhaar_number = Column(
        String(12),
        unique=True
    )

    pan_number = Column(
        String(10),
        unique=True
    )

    is_verified = Column(
        Boolean,
        default=False
    )

    member = relationship(
        "Member",
        backref="identity_proofs"
    )