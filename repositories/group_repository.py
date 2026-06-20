from models.group import Group
from models.group_member import GroupMember
from models.group_role_history import GroupRoleHistory


class GroupRepository:

    @staticmethod
    def create(db, group):
        db.add(group)
        db.commit()
        db.refresh(group)
        return group

    @staticmethod
    def get_all(db):
        return db.query(Group).all()

    @staticmethod
    def get_by_id(db, group_id):
        return (
            db.query(Group)
            .filter(Group.group_id == group_id)
            .first()
        )

    @staticmethod
    def update(db, group):
        db.commit()
        db.refresh(group)
        return group

    @staticmethod
    def get_group_member_count(
        db,
        group_id
    ):
        return (
            db.query(GroupMember)
            .filter(
                GroupMember.group_id == group_id,
                GroupMember.status == "ACTIVE"
            )
            .count()
        )

    @staticmethod
    def get_member_group(
        db,
        member_id
    ):
        return (
            db.query(GroupMember)
            .filter(
                GroupMember.member_id == member_id,
                GroupMember.status == "ACTIVE"
            )
            .first()
        )

    @staticmethod
    def add_member(
        db,
        group_member
    ):
        db.add(group_member)
        db.commit()
        db.refresh(group_member)
        return group_member

    @staticmethod
    def create_role_history(
        db,
        history
    ):
        db.add(history)
        db.commit()
        db.refresh(history)
        return history