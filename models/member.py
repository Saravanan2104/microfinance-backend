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
    secondary_number = Column(String(20), nullable=True)    
    

    member_code = Column(
        String(20),
        unique=True,
        nullable=False
    )  

    



    def __repr__(self):
        return f"<Member {self.first_name}>"
    
