from booking.repos.service_repo import ServiceRepo

class ServiceService:
    @staticmethod
    def get_all_services():
        return ServiceRepo.get_all_services()
