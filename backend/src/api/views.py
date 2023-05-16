from rest_framework.generics import UpdateAPIView, ListAPIView, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer, GroupCreateSerializer, ChangePasswordSerializer, \
    CategorySerializer, GroupParticipantSerializer, MeetingCreateSerializer, MeetingSerializer
from web.models import User, Group, Category, GroupParticipant, Meeting


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return GroupCreateSerializer
        return GroupSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserGroupView(ListAPIView):
    serializer_class = GroupParticipantSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['pk']
        role = self.request.query_params.get('role', None)
        groups = GroupParticipant.objects.filter(user_id=user_id)
        if role:
            groups = GroupParticipant.objects.filter(role=role)
        return groups

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserGroupSerializer(queryset, many=True)
        for data in serializer.data:
            group_id = data.get("group", None)
            group = get_object_or_404(Group, id=group_id)
            data["group_info"] = {"title": group.title, "city": group.city}
        return Response(serializer.data)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return MeetingCreateSerializer
        return MeetingSerializer
