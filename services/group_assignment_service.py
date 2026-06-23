from models.group_assignment import (
    GroupAssignment
)

from repositories.group_assignment_repository import (
    GroupAssignmentRepository
)


class GroupAssignmentService:

    @staticmethod
    def assign_group(
        db,
        data
    ):

        assignment = (
            GroupAssignment(
                group_id=
                data.group_id,

                rm_employee_id=
                data.rm_employee_id,

                qa_employee_id=
                data.qa_employee_id
            )
        )

        return (
            GroupAssignmentRepository.create(
                db,
                assignment
            )
        )

    @staticmethod
    def get_all(
        db
    ):
        return (
            GroupAssignmentRepository.get_all(
                db
            )
        )