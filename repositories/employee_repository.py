from models.role import Role
from models.user import User
from models.employee import Employee


class EmployeeRepository:

    @staticmethod
    def get_role_by_name(
        db,
        role_name
    ):
        return (
            db.query(Role)
            .filter(
                Role.role_name == role_name
            )
            .first()
        )

    @staticmethod
    def get_role_employee_count(
        db,
        role_id
    ):
        return (
            db.query(Employee)
            .join(User)
            .filter(
                User.role_id == role_id
            )
            .count()
        )

    @staticmethod
    def create_user(db, user):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def create_employee(
        db,
        employee
    ):
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee