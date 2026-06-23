from repositories.report_repository import (
    ReportRepository
)


class ReportService:

    @staticmethod
    def get_collection_report(db):

        return (
            ReportRepository
            .get_collection_report(db)
        )

    @staticmethod
    def get_loan_report(db):

        return (
            ReportRepository
            .get_loan_report(db)
        )

    @staticmethod
    def get_overdue_report(db):

        return (
            ReportRepository
            .get_overdue_report(db)
        )