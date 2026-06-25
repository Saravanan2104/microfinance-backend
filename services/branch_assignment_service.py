from fastapi import HTTPException

from models.branch_assignment import (
    BranchAssignment
)

from repositories.branch_assignment_repository import (
    BranchAssignmentRepository
)

from repositories.branch_repository import (
    BranchRepository
)

from repositories.employee_repository import (
    EmployeeRepository
)


class BranchAssignmentService:

    @staticmethod
    def assign_branch(
        db,
        data
    ):

        branch = (
            BranchRepository.get_by_id(
                db,
                data.branch_id
            )
        )

        if not branch:
            raise HTTPException(
                status_code=404,
                detail="Branch not found"
            )

        employee = (
            EmployeeRepository.get_by_id(
                db,
                data.employee_id
            )
        )

        if not employee:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        existing = (
            BranchAssignmentRepository.get_by_employee(
                db,
                data.employee_id
            )
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Employee already assigned to a branch"
            )

        assignment = BranchAssignment(
            branch_id=data.branch_id,
            employee_id=data.employee_id
        )

        return (
            BranchAssignmentRepository.create(
                db,
                assignment
            )
        )