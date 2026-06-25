from models.branch_assignment import (
    BranchAssignment
)


class BranchAssignmentRepository:

    @staticmethod
    def create(
        db,
        assignment
    ):
        db.add(assignment)
        db.commit()
        db.refresh(assignment)
        return assignment

    @staticmethod
    def get_by_employee(
        db,
        employee_id
    ):
        return (
            db.query(
                BranchAssignment
            )
            .filter(
                BranchAssignment.employee_id == employee_id,
                BranchAssignment.status == "ACTIVE"
            )
            .first()
        )

    @staticmethod
    def get_by_branch(
        db,
        branch_id
    ):
        return (
            db.query(
                BranchAssignment
            )
            .filter(
                BranchAssignment.branch_id == branch_id,
                BranchAssignment.status == "ACTIVE"
            )
            .all()
        )