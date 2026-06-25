from fastapi import HTTPException

from models.group import Group
from models.group_member import GroupMember
from models.group_role_history import GroupRoleHistory
from models.branch import Branch

from repositories.group_repository import GroupRepository


class GroupService:

    @staticmethod
    def create_group(db, data):

        group_count = (
            GroupRepository.get_group_count(db)
            + 1
        )

        group_code = (
            f"GRP{group_count:06d}"
        )

        branch = (
            db.query(Branch)
            .filter(
                Branch.branch_id == data.branch_id
            )
            .first()
        )

        if not branch:
            raise HTTPException(
                status_code=404,
                detail="Branch not found"
            )

        group = Group(
            group_code=group_code,

            group_name=data.group_name,

            branch_id=data.branch_id,

            location_id=branch.location_id,

            group_limit_amount=data.group_limit_amount
        )

        return GroupRepository.create(
            db,
            group
        )

    @staticmethod
    def get_all_groups(db):
        return GroupRepository.get_all(db)

    @staticmethod
    def get_group_by_id(
        db,
        group_id
    ):
        return GroupRepository.get_by_id(
            db,
            group_id
        )

    @staticmethod
    def update_group(
        db,
        group,
        data
    ):

        update_data = data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(group, key, value)

        return GroupRepository.update(
            db,
            group
        )

    @staticmethod
    def add_member_to_group(
        db,
        group_id,
        member_ids
    ):

        group = GroupRepository.get_by_id(
            db,
            group_id
        )

        if not group:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            )

        member_count = (
            GroupRepository.get_group_member_count(
                db,
                group_id
            )
        )

        if member_count + len(member_ids) > 20:
            raise HTTPException(
                status_code=400,
                detail="Group member limit reached"
            )

        added_members = []

        for member_id in member_ids:

            existing_group = (
                GroupRepository.get_member_group(
                    db,
                    member_id
                )
            )

            if existing_group:
                continue

            group_member = GroupMember(
                group_id=group_id,
                member_id=member_id
            )

            GroupRepository.add_member(
                db,
                group_member
            )

            added_members.append(member_id)

        return {
            "message": "Members added successfully",
            "member_ids": added_members
        }

    @staticmethod
    def assign_head(
        db,
        group_id,
        data
    ):

        group = GroupRepository.get_by_id(
            db,
            group_id
        )

        if not group:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            )

        member_group = (
            GroupRepository.get_member_group(
                db,
                data.member_ids
            )
        )

        if (
            not member_group
            or
            member_group.group_id != group_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Member does not belong to this group"
            )

        group.head_member_ids = data.member_ids

        GroupRepository.update(
            db,
            group
        )

        history = GroupRoleHistory(
            group_id=group_id,
            member_ids=data.member_ids,
            role_type="HEAD",
            changed_by_employee_id=
                data.changed_by_employee_id,
            remarks=data.remarks
        )

        GroupRepository.create_role_history(
            db,
            history
        )

        return group

    @staticmethod
    def assign_sub_head(
        db,
        group_id,
        data
    ):

        group = GroupRepository.get_by_id(
            db,
            group_id
        )

        if not group:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            )

        member_group = (
            GroupRepository.get_member_group(
                db,
                data.member_ids
            )
        )

        if (
            not member_group
            or
            member_group.group_id != group_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Member does not belong to this group"
            )

        group.sub_head_member_ids = data.member_ids

        GroupRepository.update(
            db,
            group
        )

        history = GroupRoleHistory(
            group_id=group_id,
            member_ids=data.member_ids,
            role_type="SUB_HEAD",
            changed_by_employee_id=
                data.changed_by_employee_id,
            remarks=data.remarks
        )

        GroupRepository.create_role_history(
            db,
            history
        )

        return group
    
    @staticmethod
    def get_group_members(db,group_id):

        group = GroupRepository.get_by_id(db,group_id)

        if not group:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            )

        return GroupRepository.get_group_members(
            db,
            group_id
        )