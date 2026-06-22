from fastapi import HTTPException

from models.group import Group
from models.group_member import GroupMember
from models.group_role_history import GroupRoleHistory

from repositories.group_repository import GroupRepository


class GroupService:

    @staticmethod
    def create_group(db, data):

        group = Group(
            group_code=data.group_code,
            group_name=data.group_name,
            branch_id=data.branch_id,
            location_id=data.location_id,
            relationship_manager_employee_id=
                data.relationship_manager_employee_id,
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

        existing_group = (
            GroupRepository.get_member_group(
                db,
                member_ids
            )
        )

        if existing_group:
            raise HTTPException(
                status_code=400,
                detail="Member already belongs to a group"
            )

        member_count = (
            GroupRepository.get_group_member_count(
                db,
                group_id
            )
        )

        if member_count >= 20:
            raise HTTPException(
                status_code=400,
                detail="Group member limit reached"
            )

        group_member = GroupMember(
            group_id=group_id,
            member_ids=member_ids
        )

        return GroupRepository.add_member(
            db,
            group_member
        )

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