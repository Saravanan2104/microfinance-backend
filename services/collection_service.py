from fastapi import HTTPException
import uuid

from models.collection import Collection

from repositories.collection_repository import (
    CollectionRepository
)


class CollectionService:

    @staticmethod
    def create_collection(
        db,
        data
    ):

        schedule = (
            CollectionRepository
            .get_repayment_schedule(
                db,
                data.repayment_schedule_id
            )
        )

        if not schedule:
            raise HTTPException(
                status_code=404,
                detail="Repayment schedule not found"
            )

        receipt_number = (
            f"RCPT-{uuid.uuid4().hex[:8].upper()}"
        )

        collection = Collection(
            loan_account_id=
                data.loan_account_id,

            repayment_schedule_id=
                data.repayment_schedule_id,

            member_id=
                data.member_id,

            collection_date=
                data.collection_date,

            collected_amount=
                data.collected_amount,

            collection_mode=
                data.collection_mode,

            receipt_number=
                receipt_number,

            remarks=
                data.remarks,

            collected_by_employee_id=
                data.collected_by_employee_id
        )

        created_collection = (
            CollectionRepository.create(
                db,
                collection
            )
        )

        payment_amount = (
            data.collected_amount
        )

        current_schedule = schedule

        while (
            payment_amount > 0
            and
            current_schedule
        ):

            remaining_amount = (
                current_schedule.total_amount
                -
                current_schedule.paid_amount
            )

            if payment_amount >= remaining_amount:

                current_schedule.paid_amount += (
                    remaining_amount
                )

                current_schedule.balance_amount = 0

                current_schedule.status = (
                    "PAID"
                )

                payment_amount -= (
                    remaining_amount
                )

                CollectionRepository.update_repayment_schedule(
                    db,
                    current_schedule
                )

                current_schedule = (
                    CollectionRepository.get_next_installment(
                        db,
                        current_schedule.loan_account_id,
                        current_schedule.installment_no
                    )
                )

            else:

                current_schedule.paid_amount += (
                    payment_amount
                )

                current_schedule.balance_amount = (
                    current_schedule.total_amount
                    -
                    current_schedule.paid_amount
                )

                current_schedule.status = (
                    "PARTIALLY_PAID"
                )

                CollectionRepository.update_repayment_schedule(
                    db,
                    current_schedule
                )

                payment_amount = 0

        return created_collection

    @staticmethod
    def get_collections_by_loan_account(
        db,
        loan_account_id
    ):
        return (
            CollectionRepository
            .get_by_loan_account(
                db,
                loan_account_id
            )
        )