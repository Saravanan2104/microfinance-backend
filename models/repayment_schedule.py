from sqlalchemy import (Column,Integer,Float,Date,String,ForeignKey)

from database.base import Base


class RepaymentSchedule(Base):
    __tablename__ = "repayment_schedules"

    repayment_schedule_id = Column(Integer,primary_key=True,index=True)

    loan_account_id = Column(Integer,ForeignKey("loan_accounts.loan_account_id"),nullable=False)

    installment_no = Column(Integer,nullable=False)

    due_date = Column(Date,nullable=False)

    principal_amount = Column(Float,default=0)

    interest_amount = Column(Float,default=0)

    total_amount = Column(Float,default=0)

    paid_amount = Column(Float,default=0)

    balance_amount = Column(Float,default=0)

    status = Column(String(20),default="PENDING")