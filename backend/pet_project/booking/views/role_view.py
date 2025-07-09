from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.role_serializers import RoleSerializer
from booking.services.role_services import RoleService

class RoleListCreateView(APIView):
    def get(self, request):
        roles = RoleService.list_roles()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            role = RoleService.create_role(serializer.validated_data)
            return Response(RoleSerializer(role).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetailView(APIView):
    def get(self, request, role_id):
        role = RoleService.retrieve_role(role_id)
        if role:
            return Response(RoleSerializer(role).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, role_id):
        role = RoleService.retrieve_role(role_id)
        if not role:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            updated = RoleService.update_role(role, serializer.validated_data)
            return Response(RoleSerializer(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, role_id):
        role = RoleService.retrieve_role(role_id)
        if not role:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        RoleService.delete_role(role)
        return Response(status=status.HTTP_204_NO_CONTENT)
