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