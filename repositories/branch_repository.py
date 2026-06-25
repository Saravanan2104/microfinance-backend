from models.branch import Branch


class BranchRepository:

    @staticmethod
    def create(
        db,
        branch
    ):
        db.add(branch)
        db.commit()
        db.refresh(branch)
        return branch

    @staticmethod
    def get_all(db):
        return (
            db.query(Branch)
            .all()
        )

    @staticmethod
    def get_by_id(
        db,
        branch_id
    ):
        return (
            db.query(Branch)
            .filter(
                Branch.branch_id == branch_id
            )
            .first()
        )

    @staticmethod
    def update(
        db,
        branch
    ):
        db.commit()
        db.refresh(branch)
        return branch

    @staticmethod
    def get_count(db):
        return (
            db.query(Branch)
            .count()
        )