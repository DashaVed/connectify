from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers import TokenResponseSerializer, \
    LoginSerializer, UserSerializer, GroupSerializer
from web.models import User, Group


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
