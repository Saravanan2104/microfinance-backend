from schemas.employee_schema import EmployeeCreate


from services.employee_service import EmployeeService


class BranchManagerService:

    @staticmethod
    def create_branch_manager(
        db,
        data
    ):

        employee = EmployeeCreate(

            role_name="BM",

            password=data.password,

            first_name=data.first_name,

            last_name=data.last_name,

            email=data.email,

            phone=data.phone
        )

        return EmployeeService.create_employee(
            db=db,
            data=employee
        )