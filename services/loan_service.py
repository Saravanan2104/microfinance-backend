from fastapi import HTTPException

from models.loan_application import LoanApplication
from models.loan_approval_history import LoanApprovalHistory
from models.loan_account import LoanAccount

from repositories.loan_repository import LoanRepository
from repositories.group_repository import GroupRepository
from services.repayment_service import RepaymentService
from repositories.repayment_repository import RepaymentRepository


class LoanService:

    @staticmethod
    def create_loan_application(
        db,
        data
    ):

        group = GroupRepository.get_by_id(
            db,
            data.group_id
        )

        if not group:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            )

        if group.status != "ACTIVE":
            raise HTTPException(
                status_code=400,
                detail="Group is not active"
            )

        member_group = (
            GroupRepository.get_member_group(
                db,
                data.member_id
            )
        )

        if (
            not member_group
            or
            member_group.group_id != data.group_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Member does not belong to this group"
            )

        active_loan = (
            LoanRepository.get_active_loan_by_member(
                db,
                data.member_id
            )
        )

        if active_loan:
            raise HTTPException(
                status_code=400,
                detail="Member already has an active loan"
            )

        if (
            data.requested_amount >
            group.group_limit_amount
        ):
            raise HTTPException(
                status_code=400,
                detail="Requested amount exceeds group limit"
            )

        loan_application = LoanApplication(
            application_number=data.application_number,
            member_id=data.member_id,
            group_id=data.group_id,
            requested_amount=data.requested_amount,
            loan_purpose=data.loan_purpose,
            created_by=data.created_by
        )

        return LoanRepository.create(
            db,
            loan_application
        )

    @staticmethod
    def get_all_loan_applications(db):
        return LoanRepository.get_all(db)

    @staticmethod
    def get_loan_application_by_id(
        db,
        loan_application_id
    ):
        return LoanRepository.get_by_id(
            db,
            loan_application_id
        )

    @staticmethod
    def update_loan_application(
        db,
        loan_application,
        data
    ):

        if loan_application.application_status != "DRAFT":
            raise HTTPException(
                status_code=400,
                detail="Only draft applications can be updated"
            )

        update_data = data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                loan_application,
                key,
                value
            )

        return LoanRepository.update(
            db,
            loan_application
        )

    @staticmethod
    def submit_application(
        db,
        loan_application
    ):

        if loan_application.application_status != "DRAFT":
            raise HTTPException(
                status_code=400,
                detail="Application already submitted"
            )

        loan_application.application_status = (
            "SUBMITTED"
        )

        return LoanRepository.update(
            db,
            loan_application
        )

    @staticmethod
    def rm_approve(
        db,
        loan_application,
        data
    ):

        if (
            loan_application.application_status
            !=
            "SUBMITTED"
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid application status"
            )

        loan_application.application_status = (
            "RM_APPROVED"
        )

        LoanRepository.update(
            db,
            loan_application
        )

        history = LoanApprovalHistory(
            loan_application_id=
                loan_application.loan_application_id,
            approved_by_employee_id=
                data.employee_id,
            action_type="RM_APPROVED",
            remarks=data.remarks
        )

        LoanRepository.create_approval_history(
            db,
            history
        )

        return loan_application
    
    @staticmethod
    def get_member_loans(
        db,
        member_id
    ):
        return LoanRepository.get_loans_by_member(
            db,
            member_id
        )

    @staticmethod
    def bm_approve(
        db,
        loan_application,
        data
    ):

        if (
            loan_application.application_status
            !=
            "RM_APPROVED"
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid application status"
            )

        loan_application.application_status = (
            "BM_APPROVED"
        )

        LoanRepository.update(
            db,
            loan_application
        )

        history = LoanApprovalHistory(
            loan_application_id=
                loan_application.loan_application_id,
            approved_by_employee_id=
                data.employee_id,
            action_type="BM_APPROVED",
            remarks=data.remarks
        )

        LoanRepository.create_approval_history(
            db,
            history
        )

        return loan_application
    
    @staticmethod
    def close_loan(
        db,
        loan_account_id
    ):

        loan_account = (
            LoanRepository
            .get_loan_account_by_id(
                db,
                loan_account_id
            )
        )

        if not loan_account:
            raise HTTPException(
                status_code=404,
                detail="Loan account not found"
            )

        schedules = (
            RepaymentRepository
            .get_by_loan_account(
                db,
                loan_account_id
            )
        )

        pending = [
            s for s in schedules
            if s.status != "PAID"
        ]

        if pending:
            raise HTTPException(
                status_code=400,
                detail=
                "Loan cannot be closed. Pending installments exist."
            )

        loan_account.loan_status = (
            "CLOSED"
        )

        LoanRepository.update_loan_account(
            db,
            loan_account
        )

        return {
            "loan_account_id":
                loan_account.loan_account_id,

            "loan_status":
                loan_account.loan_status,

            "message":
                "Loan closed successfully"
        }

    @staticmethod
    def admin_approve(
        db,
        loan_application,
        data
    ):

        if (
            loan_application.application_status
            !=
            "BM_APPROVED"
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid application status"
            )

        loan_application.application_status = (
            "ADMIN_APPROVED"
        )

        LoanRepository.update(
            db,
            loan_application
        )

        history = LoanApprovalHistory(
            loan_application_id=
                loan_application.loan_application_id,
            approved_by_employee_id=
                data.employee_id,
            action_type="ADMIN_APPROVED",
            remarks=data.remarks
        )

        LoanRepository.create_approval_history(
            db,
            history
        )

        loan_account = LoanAccount(
            loan_application_id=
                loan_application.loan_application_id,

            loan_account_number=
                f"LN-{loan_application.loan_application_id}",

            sanctioned_amount=
                loan_application.requested_amount,

            interest_rate=12,

            tenure_months=12,

            emi_amount=
                loan_application.requested_amount / 12
        )

        LoanRepository.create_loan_account(
            db,
            loan_account
        )

        RepaymentService.generate_schedule(
            db,
            loan_account
        )

        loan_application.application_status = (
            "SANCTIONED"
        )

        return LoanRepository.update(
            db,
            loan_application
        )