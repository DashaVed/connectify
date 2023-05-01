from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers import TokenResponseSerializer, \
    LoginSerializer, UserSerializer, GroupSerializer
from web.models import User, Group


class UserViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        user = User.objects.filter(id=pk)
        if user:
            serializer = UserSerializer(user[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
