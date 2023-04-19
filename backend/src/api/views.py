from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes,
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from api.serializers import RegistrationSerializer, TokenResponseSerializer, LoginSerializer


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


@api_view(["POST"])
@permission_classes([])
def auth_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(request, **serializer.validated_data)
    if user is None:
        raise AuthenticationFailed()
    token, _ = Token.objects.get_or_create(user=user)
    response_data = {"token": token.key}
    response_serializer = TokenResponseSerializer(response_data)
    return Response(response_serializer.data)



