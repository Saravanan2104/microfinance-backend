from datetime import date
from dateutil.relativedelta import relativedelta

from models.repayment_schedule import (
    RepaymentSchedule
)

from repositories.repayment_repository import (
    RepaymentRepository
)


class RepaymentService:

    @staticmethod
    def generate_schedule(
        db,
        loan_account
    ):

        schedules = []

        monthly_principal = (
            loan_account.sanctioned_amount
            /
            loan_account.tenure_months
        )

        monthly_interest = (
            (
                loan_account.sanctioned_amount
                *
                loan_account.interest_rate
            )
            /
            100
        ) / 12

        for installment_no in range(
            1,
            loan_account.tenure_months + 1
        ):

            due_date = (
                date.today()
                +
                relativedelta(
                    months=installment_no
                )
            )

            total_amount = (
                monthly_principal
                +
                monthly_interest
            )

            schedule = RepaymentSchedule(
                loan_account_id=
                    loan_account.loan_account_id,

                installment_no=
                    installment_no,

                due_date=
                    due_date,

                principal_amount=
                    monthly_principal,

                interest_amount=
                    monthly_interest,

                total_amount=
                    total_amount,

                paid_amount=0,

                balance_amount=
                    total_amount,

                status="PENDING"
            )

            schedules.append(
                schedule
            )

        return (
            RepaymentRepository.create_many(
                db,
                schedules
            )
        )

    @staticmethod
    def get_schedule_by_loan_account(
        db,
        loan_account_id
    ):
        return (
            RepaymentRepository
            .get_by_loan_account(
                db,
                loan_account_id
            )
        )