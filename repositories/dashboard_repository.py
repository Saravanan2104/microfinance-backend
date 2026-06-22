from models.member import Member
from models.group import Group
from models.loan_application import LoanApplication
from models.loan_account import LoanAccount


class DashboardRepository:

    @staticmethod
    def get_summary(db):

        total_members = db.query(Member).count()

        total_groups = db.query(Group).count()

        total_loan_applications = (
            db.query(LoanApplication).count()
        )

        active_loans = (
            db.query(LoanAccount)
            .filter(
                LoanAccount.loan_status == "ACTIVE"
            )
            .count()
        )

        pending_approvals = (
            db.query(LoanApplication)
            .filter(
                LoanApplication.application_status.in_(
                    [
                        "SUBMITTED",
                        "RM_APPROVED",
                        "BM_APPROVED"
                    ]
                )
            )
            .count()
        )

        return {
            "total_members": total_members,
            "total_groups": total_groups,
            "total_loan_applications": total_loan_applications,
            "active_loans": active_loans,
            "pending_approvals": pending_approvals
        }