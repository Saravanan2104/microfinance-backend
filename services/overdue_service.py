from repositories.repayment_repository import (
    RepaymentRepository
)


class OverdueService:

    @staticmethod
    def get_overdue_installments(
        db
    ):

        installments = (
            RepaymentRepository
            .get_overdue_installments(
                db
            )
        )

        return installments