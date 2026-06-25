from fastapi import HTTPException

from models.branch import Branch

from repositories.branch_repository import (
    BranchRepository
)


class BranchService:

    @staticmethod
    def create_branch(
        db,
        data
    ):

        branch_count = (
            BranchRepository.get_count(db)
            + 1
        )

        branch_code = (
            f"BR{branch_count:03d}"
        )

        branch = Branch(

            branch_code=branch_code,

            branch_name=data.branch_name
        )

        return (
            BranchRepository.create(
                db,
                branch
            )
        )

    @staticmethod
    def get_all_branches(db):

        return (
            BranchRepository.get_all(db)
        )

    @staticmethod
    def get_branch_by_id(
        db,
        branch_id
    ):

        branch = (
            BranchRepository.get_by_id(
                db,
                branch_id
            )
        )

        if not branch:
            raise HTTPException(
                status_code=404,
                detail="Branch not found"
            )

        return branch

    @staticmethod
    def update_branch(
        db,
        branch,
        data
    ):

        branch.branch_name = (
            data.branch_name
        )

        return (
            BranchRepository.update(
                db,
                branch
            )
        )