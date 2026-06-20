from models.member import Member


class MemberRepository:

    @staticmethod
    def create(db, member):
        db.add(member)
        db.commit()
        db.refresh(member)
        return member

    @staticmethod
    def get_all(db):
        return db.query(Member).all()

    @staticmethod
    def get_by_id(db, member_id):
        return (
            db.query(Member)
            .filter(Member.member_id == member_id)
            .first()
        )

    @staticmethod
    def update(db, member):
        db.commit()
        db.refresh(member)
        return member