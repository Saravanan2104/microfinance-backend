from fastapi import FastAPI

from seed import seed_data

from database.base import Base
from database.connection import engine

from models.role import Role
from models.user import User

from models.branch import Branch
from models.location import Location
from models.employee import Employee

from models.member import Member
from models.member_address import MemberAddress
from models.member_identity_proof import MemberIdentityProof
from models.member_bank_account import MemberBankAccount
from models.member_nominee import MemberNominee
from models.member_document import MemberDocument

from models.loan_application import LoanApplication
from models.loan_document import LoanDocument
from models.loan_approval_history import LoanApprovalHistory
from models.loan_account import LoanAccount


from models.repayment_schedule import RepaymentSchedule
from models.collection import Collection
from models.collection_transaction import CollectionTransaction
from models.notification import Notification


from models.group import Group
from models.group_member import GroupMember
from models.group_role_history import GroupRoleHistory

from routers.member_router import router as member_router
from routers.group_router import router as group_router
from routers.loan_router import router as loan_router
from routers.dashboard_router import router as dashboard_router
from routers.repayment_router import router as repayment_router
from routers.collection_router import router as collection_router
from routers.overdue_router import router as overdue_router
from routers.dashboard_router import router as dashboard_router
from routers.report_router import router as report_router
from routers.employee_router import router as employee_router
from routers.role_router import router as role_router
from routers.auth_router import router as auth_router
from routers.group_assignment_router import router as group_assignment_router
from routers.branch_router import router as branch_router
from routers.branch_assignment_router import router as branch_assignment_router





from fastapi.middleware.cors import CORSMiddleware


# Table creation
Base.metadata.create_all(bind=engine)

from database.dependencies import (
    SessionLocal
)

db = SessionLocal()

seed_data(db)

db.close()



app = FastAPI(
    title="Group Loan Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers

app.include_router(role_router)
app.include_router(branch_router)
#app.include_router(location_router)
app.include_router(employee_router)
app.include_router(member_router)
app.include_router(group_router)
app.include_router(loan_router)
app.include_router(collection_router)
app.include_router(report_router)
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(group_assignment_router)
app.include_router(branch_assignment_router)



@app.get("/")
def home():
    return {
        "message": "Group Loan Management API Running"
    }