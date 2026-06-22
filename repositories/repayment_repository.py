from models.repayment_schedule import (
    RepaymentSchedule
)


class RepaymentRepository:

    @staticmethod
    def create(
        db,
        repayment_schedule
    ):
        db.add(repayment_schedule)
        db.commit()
        db.refresh(repayment_schedule)

        return repayment_schedule

    @staticmethod
    def create_many(
        db,
        schedules
    ):
        db.add_all(schedules)
        db.commit()

        return schedules

    @staticmethod
    def get_by_loan_account(
        db,
        loan_account_id
    ):
        return (
            db.query(RepaymentSchedule)
            .filter(
                RepaymentSchedule.loan_account_id
                ==
                loan_account_id
            )
            .all()
        )