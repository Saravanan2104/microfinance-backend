from models.collection import Collection
from models.repayment_schedule import (
    RepaymentSchedule
)


class CollectionRepository:

    @staticmethod
    def create(
        db,
        collection
    ):
        db.add(collection)
        db.commit()
        db.refresh(collection)

        return collection

    @staticmethod
    def get_repayment_schedule(
        db,
        repayment_schedule_id
    ):
        return (
            db.query(RepaymentSchedule)
            .filter(
                RepaymentSchedule.repayment_schedule_id
                ==
                repayment_schedule_id
            )
            .first()
        )

    @staticmethod
    def update_repayment_schedule(
        db,
        schedule
    ):
        db.commit()
        db.refresh(schedule)

        return schedule

    @staticmethod
    def get_by_loan_account(
        db,
        loan_account_id
    ):
        return (
            db.query(Collection)
            .filter(
                Collection.loan_account_id
                ==
                loan_account_id
            )
            .all()
        )
    
    @staticmethod
    def get_next_installment(
        db,
        loan_account_id,
        installment_no
    ):
        return (
            db.query(RepaymentSchedule)
            .filter(
                RepaymentSchedule.loan_account_id == loan_account_id,
                RepaymentSchedule.installment_no > installment_no
            )
            .order_by(
                RepaymentSchedule.installment_no
            )
            .first()
        )