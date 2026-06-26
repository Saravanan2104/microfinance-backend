from models.group_assignment import (
    GroupAssignment
)


class GroupAssignmentRepository:

    @staticmethod
    def create(
        db,
        assignment
    ):
        db.add(assignment)
        db.commit()
        db.refresh(
            assignment
        )
        return assignment

    @staticmethod
    def get_all(db):
        return (
            db.query(
                GroupAssignment
            ).all()
        )
    
    @staticmethod
    def get_by_rm_employee(
        db,
        employee_id
    ):
        return (
            db.query(GroupAssignment)
            .filter(
                GroupAssignment.rm_employee_id == employee_id,
                GroupAssignment.status == "ACTIVE"
            )
            .all()
        )

    @staticmethod
    def get_by_qa_employee(
        db,
        employee_id
    ):
        return (
            db.query(GroupAssignment)
            .filter(
                GroupAssignment.qa_employee_id == employee_id,
                GroupAssignment.status == "ACTIVE"
            )
            .all()
        )