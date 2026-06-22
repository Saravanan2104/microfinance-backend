from repositories.dashboard_repository import (
    DashboardRepository
)


class DashboardService:

    @staticmethod
    def get_dashboard(
        db
    ):

        return {

            "total_members":
                DashboardRepository
                .get_total_members(db),

            "total_groups":
                DashboardRepository
                .get_total_groups(db),

            "active_loans":
                DashboardRepository
                .get_active_loans(db),

            "overdue_installments":
                DashboardRepository
                .get_overdue_installments(
                    db
                ),

            "total_collections":
                DashboardRepository
                .get_total_collections(
                    db
                )
        }