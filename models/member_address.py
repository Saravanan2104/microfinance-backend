from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database.base import Base


class MemberAddress(Base):
    __tablename__ = "member_addresses"

    member_address_id = Column(Integer,primary_key=True,index=True)

    member_id = Column(Integer,ForeignKey("members.member_id"),nullable=False)

    address_type = Column(String(20),nullable=False)

    door_no = Column(String(50))

    street = Column(String(255))

    area = Column(String(255))

    city = Column(String(100))

    state = Column(String(100))

    pincode = Column(String(20))

    member = relationship( "Member",backref="addresses")