from sqlalchemy import Column, Integer, String

from database.base import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role_name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f"<Role {self.role_name}>"