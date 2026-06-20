from models.member import Member

from repositories.member_repository import MemberRepository


class MemberService:

    @staticmethod
    def create_member(db, data):

        member_count = len(
            MemberRepository.get_all(db)
        ) + 1

        member_code = f"MBR{member_count:06d}"

        member = Member(
            member_code=member_code,

            first_name=data.first_name,
            last_name=data.last_name,

            dob=data.dob,
            gender=data.gender,
            marital_status=data.marital_status,

            phone=data.phone,
            whatsapp_number=data.whatsapp_number,
            secondary_number=data.secondary_number,

            email=data.email,

            password_hash=data.password,

            is_active=True
        )

        return MemberRepository.create(
            db=db,
            member=member
        )

    @staticmethod
    def get_all_members(db):
        return MemberRepository.get_all(db)

    @staticmethod
    def get_member_by_id(
        db,
        member_id
    ):
        return MemberRepository.get_by_id(
            db,
            member_id
        )

    @staticmethod
    def update_member(
        db,
        member,
        data
    ):

        update_data = data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(member, key, value)

        return MemberRepository.update(
            db,
            member
        )