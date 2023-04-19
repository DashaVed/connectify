from django.contrib.auth import authenticate
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.serializers import RegistrationSerializer, TokenResponseSerializer


@api_view(['POST'])
@permission_classes([])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response(
                {'status': 'ok',
                 'message': 'Вы успешно зарегистрировались'
                 }
            )
    return Response(
        {'status': 'error',
         'message': 'Пользователь с таким email уже существует. '
                    'Авторизуйтесь или введите другой email'
         }
    )



