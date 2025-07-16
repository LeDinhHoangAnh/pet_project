import jwt
from django.conf import settings
from booking.models.users import Users
from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped(self, request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return Response({'detail': 'Missing or invalid Authorization header'},
                            status=status.HTTP_401_UNAUTHORIZED)

        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # Bắt buộc phải có claim 'id'
            user_id = payload.get('id')
            if not user_id:
                raise jwt.DecodeError('Token missing user id')
            request.user = Users.objects.get(id=user_id)
        except jwt.ExpiredSignatureError:
            return Response({'detail': 'Token expired'},
                            status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            return Response({'detail': 'Invalid token'},
                            status=status.HTTP_401_UNAUTHORIZED)
        except Users.DoesNotExist:
            return Response({'detail': 'User not found'},
                            status=status.HTTP_404_NOT_FOUND)

        return view_func(self, request, *args, **kwargs)
    return _wrapped