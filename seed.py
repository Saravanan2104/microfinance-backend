from sqlalchemy.orm import Session

from models.role import Role
from models.user import User

from core.security import hash_password


def seed_data(db: Session):

    roles = [
        "ADMIN",
        "BM",
        "RM",
        "QA"
    ]

    for role_name in roles:

        existing_role = (
            db.query(Role)
            .filter(
                Role.role_name == role_name
            )
            .first()
        )

        if not existing_role:

            db.add(
                Role(
                    role_name=role_name
                )
            )

    db.commit()

    admin_role = (
        db.query(Role)
        .filter(
            Role.role_name == "ADMIN"
        )
        .first()
    )

    admin_user = (
        db.query(User)
        .filter(
            User.username == "admin"
        )
        .first()
    )

    if not admin_user:

        admin_user = User(
            name="System Admin",

            username="admin",

            password=hash_password(
                "admin123"
            ),

            email="admin@system.com",

            phone="0987654321",

            role_id=admin_role.role_id
        )

        db.add(admin_user)

        db.commit()

        print(
            "Admin user created"
        )