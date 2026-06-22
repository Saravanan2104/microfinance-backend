from repositories.dashboard_repository import (
    DashboardRepository
)


class DashboardService:

    @staticmethod
    def get_summary(db):

        return DashboardRepository.get_summary(
            db
        )