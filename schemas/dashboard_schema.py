from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):
    total_members: int
    total_groups: int
    total_loan_applications: int
    active_loans: int
    pending_approvals: int