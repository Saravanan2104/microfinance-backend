from sqlalchemy import Column,Integer,String,Date, Boolean
from database.base import Base


class Member(Base):
    __tablename__ = "members"

    member_id = Column(Integer,primary_key=True,index=True)

    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=True)

    dob = Column(Date,nullable=True)
    gender = Column(String(20),nullable=True)

    marital_status = Column(String(20),nullable=True)

    phone = Column(String(20),unique=True,nullable=False)
    whatsapp_number = Column(String(20),nullable=True)
    secondary_number = Column(String(20), nullable=True)
    
    email = Column(String(255),unique=True,nullable=True)

    member_code = Column(
        String(20),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )



    def __repr__(self):
        return f"<Member {self.first_name}>"
    
