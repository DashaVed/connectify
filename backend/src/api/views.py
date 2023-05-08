from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers import TokenResponseSerializer, \
    LoginSerializer, UserSerializer, GroupSerializer, GroupCreateSerializer
from web.models import User, Group


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return GroupCreateSerializer
        return GroupSerializer
