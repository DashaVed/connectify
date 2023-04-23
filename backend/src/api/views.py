from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from api.serializers import RegistrationSerializer, TokenResponseSerializer, LoginSerializer, UserSerializer
from web.models import User


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


class UserViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        user = User.objects.filter(id=pk)
        if user:
            serializer = UserSerializer(user[0])
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)




