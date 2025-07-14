from booking.models.services import Services

class ServiceRepo:
    @staticmethod
    def get_all_services():
        return Services.objects.all()
