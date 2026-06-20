from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database.base import Base


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_code = Column(
        String(50),
        unique=True,
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100)
    )

    email = Column(
        String(255),
        unique=True
    )

    phone = Column(
        String(20),
        unique=True
    )

    branch_id = Column(
        Integer,
        ForeignKey("branches.branch_id")
    )

    location_id = Column(
        Integer,
        ForeignKey("locations.location_id")
    )

    manager_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True
    )

    user = relationship("User")

    branch = relationship("Branch")

    location = relationship("Location")