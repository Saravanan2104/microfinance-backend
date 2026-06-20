from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class LoanDocument(Base):
    __tablename__ = "loan_documents"

    loan_document_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    loan_application_id = Column(
        Integer,
        ForeignKey("loan_applications.loan_application_id"),
        nullable=False
    )

    document_type = Column(
        String(100),
        nullable=False
    )

    file_name = Column(
        String(255),
        nullable=False
    )

    file_url = Column(
        String(1000),
        nullable=False
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    loan_application = relationship(
        "LoanApplication"
    )