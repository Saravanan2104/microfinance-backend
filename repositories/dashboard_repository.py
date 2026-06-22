from sqlalchemy import func

from models.member import Member
from models.group import Group
from models.loan_account import LoanAccount
from models.collection import Collection
from models.repayment_schedule import (
    RepaymentSchedule
)


class DashboardRepository:

    @staticmethod
    def get_total_members(db):

        return (
            db.query(Member)
            .count()
        )

    @staticmethod
    def get_total_groups(db):

        return (
            db.query(Group)
            .count()
        )

    @staticmethod
    def get_active_loans(db):

        return (
            db.query(LoanAccount)
            .filter(
                LoanAccount.loan_status
                ==
                "ACTIVE"
            )
            .count()
        )

    @staticmethod
    def get_overdue_installments(db):

        return (
            db.query(
                RepaymentSchedule
            )
            .filter(
                RepaymentSchedule.status
                ==
                "OVERDUE"
            )
            .count()
        )

    @staticmethod
    def get_total_collections(db):

        amount = (
            db.query(
                func.sum(
                    Collection.collected_amount
                )
            )
            .scalar()
        )

        return amount or 0