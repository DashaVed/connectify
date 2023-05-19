from rest_framework.generics import UpdateAPIView, ListAPIView, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer, GroupCreateSerializer, ChangePasswordSerializer, \
    CategorySerializer, GroupParticipantSerializer, MeetingChangeSerializer, MeetingSerializer, \
    MeetingParticipantSerializer, GroupUpdateSerializer
from web.models import User, Group, Category, GroupParticipant, Meeting, MeetingParticipant


class EnablePartialUpdateMixin:

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class GroupViewSet(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return GroupCreateSerializer
        if self.action == 'update':
            return GroupUpdateSerializer
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
        serializer = GroupParticipantSerializer(queryset, many=True)
        for data in serializer.data:
            group_id = data.get("group", None)
            group = get_object_or_404(Group, id=group_id)
            data["group_info"] = {"title": group.title, "city": group.city}
        return Response(serializer.data)


class MeetingViewSet(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = Meeting.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MeetingChangeSerializer
        return MeetingSerializer


class UserMeetingView(ListAPIView):
    serializer_class = MeetingParticipantSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['pk']
        role = self.request.query_params.get('role', None)
        meetings = MeetingParticipant.objects.filter(user_id=user_id)
        if role:
            meetings = MeetingParticipant.objects.filter(role=role)
        return meetings

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MeetingParticipantSerializer(queryset, many=True)
        for data in serializer.data:
            meeting_id = data.get("meeting", None)
            meeting = get_object_or_404(Meeting, id=meeting_id)
            data["meeting_info"] = {
                "title": meeting.title,
                "date": meeting.date,
                "is_online": meeting.is_online
            }
        return Response(serializer.data)


class AddUserGroupView(UpdateAPIView):
    serializer_class = GroupParticipantSerializer
    queryset = GroupParticipant.objects.all()


class AddUserMeetingView(UpdateAPIView):
    serializer_class = MeetingParticipantSerializer
    queryset = MeetingParticipant.objects.all()
