from fastapi import HTTPException

from models.user import User
from models.employee import Employee

from repositories.employee_repository import (
    EmployeeRepository
)
from core.security import hash_password


class EmployeeService:

    @staticmethod
    def create_employee(
        db,
        data
    ):
        
        

        role = (
            EmployeeRepository.get_role_by_name(
                db,
                data.role_name
            )
        )

        if not role:
            raise HTTPException(
                status_code=404,
                detail="Role not found"
            )

        count = (
            EmployeeRepository
            .get_role_employee_count(
                db,
                role.role_id
            )
        ) + 1

        prefix = (
            data.role_name.upper()
        )

        employee_code = (
            f"{prefix}{count:03d}"
        )

        username = (
            f"{data.role_name.lower()}{count:03d}"
        )

        user = User(
            name=
                f"{data.first_name} {data.last_name or ''}",

            username=username,

            password=hash_password(data.password),

            email=data.email,

            phone=data.phone,

            role_id=role.role_id
        )

        created_user = (
            EmployeeRepository.create_user(
                db,
                user
            )
        )

        employee = Employee(
            employee_code=
                employee_code,

            user_id=
                created_user.user_id,

            first_name=
                data.first_name,

            last_name=
                data.last_name,

            email=
                data.email,

            phone=
                data.phone
        )

        created_employee = (
            EmployeeRepository.create_employee(
                db,
                employee
            )
        )

        return {
            "employee_id":
                created_employee.employee_id,

            "employee_code":
                employee_code,

            "username":
                username,

            "role":
                data.role_name,

            "message":
                "Employee created successfully"
        }
    
    @staticmethod
    def get_all_employees(db):
        return EmployeeRepository.get_all_employees(db)