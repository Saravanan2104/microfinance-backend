from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from datetime import datetime

from database.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    recipient_type = Column(
        String(50),
        nullable=False
    )

    recipient_id = Column(
        Integer,
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    message = Column(
        String(1000),
        nullable=False
    )

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )