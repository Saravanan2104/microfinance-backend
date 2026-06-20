from models.loan_application import LoanApplication
from models.loan_approval_history import LoanApprovalHistory
from models.loan_account import LoanAccount


class LoanRepository:

    @staticmethod
    def create(db, loan_application):
        db.add(loan_application)
        db.commit()
        db.refresh(loan_application)
        return loan_application

    @staticmethod
    def get_all(db):
        return db.query(
            LoanApplication
        ).all()

    @staticmethod
    def get_by_id(
        db,
        loan_application_id
    ):
        return (
            db.query(LoanApplication)
            .filter(
                LoanApplication.loan_application_id
                ==
                loan_application_id
            )
            .first()
        )

    @staticmethod
    def update(
        db,
        loan_application
    ):
        db.commit()
        db.refresh(loan_application)
        return loan_application

    @staticmethod
    def create_approval_history(
        db,
        history
    ):
        db.add(history)
        db.commit()
        db.refresh(history)
        return history

    @staticmethod
    def create_loan_account(
        db,
        loan_account
    ):
        db.add(loan_account)
        db.commit()
        db.refresh(loan_account)
        return loan_account

    @staticmethod
    def get_active_loan_by_member(
        db,
        member_id
    ):
        return (
            db.query(LoanAccount)
            .join(
                LoanApplication,
                LoanAccount.loan_application_id
                ==
                LoanApplication.loan_application_id
            )
            .filter(
                LoanApplication.member_id
                ==
                member_id,
                LoanAccount.loan_status
                ==
                "ACTIVE"
            )
            .first()
        )