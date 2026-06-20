from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database.base import Base


class Location(Base):
    __tablename__ = "locations"

    location_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    location_name = Column(
        String(255),
        nullable=False
    )

    branch_id = Column(
        Integer,
        ForeignKey("branches.branch_id"),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    branch = relationship(
        "Branch"
    )