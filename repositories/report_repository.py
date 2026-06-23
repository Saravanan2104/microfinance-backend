from sqlalchemy import func

from models.collection import Collection
from models.loan_account import LoanAccount
from models.repayment_schedule import (
    RepaymentSchedule
)


class ReportRepository:

    @staticmethod
    def get_collection_report(db):

        total_collections = (
            db.query(
                func.sum(
                    Collection.collected_amount
                )
            )
            .scalar()
        ) or 0

        total_transactions = (
            db.query(Collection)
            .count()
        )

        return {
            "total_collections":
                total_collections,

            "total_transactions":
                total_transactions
        }

    @staticmethod
    def get_loan_report(db):

        total_loans = (
            db.query(LoanAccount)
            .count()
        )

        active_loans = (
            db.query(LoanAccount)
            .filter(
                LoanAccount.loan_status
                ==
                "ACTIVE"
            )
            .count()
        )

        closed_loans = (
            db.query(LoanAccount)
            .filter(
                LoanAccount.loan_status
                ==
                "CLOSED"
            )
            .count()
        )

        return {
            "total_loans":
                total_loans,

            "active_loans":
                active_loans,

            "closed_loans":
                closed_loans
        }

    @staticmethod
    def get_overdue_report(db):

        overdue_installments = (
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

        overdue_amount = (
            db.query(
                func.sum(
                    RepaymentSchedule.balance_amount
                )
            )
            .filter(
                RepaymentSchedule.status
                ==
                "OVERDUE"
            )
            .scalar()
        ) or 0

        return {
            "overdue_installments":
                overdue_installments,

            "overdue_amount":
                overdue_amount
        }