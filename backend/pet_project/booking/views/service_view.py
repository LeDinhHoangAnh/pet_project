from rest_framework.views import APIView
from rest_framework.response import Response
from booking.services.service_service import ServiceService
from booking.serializers.service_serializer import ServiceSerializer

class ServiceListView(APIView):
    def get(self, request):
        services = ServiceService.get_all_services()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
