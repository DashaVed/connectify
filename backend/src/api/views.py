from datetime import datetime

from rest_framework.generics import UpdateAPIView, ListAPIView, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer, GroupChangeSerializer, ChangePasswordSerializer, \
    CategorySerializer, GroupParticipantSerializer, MeetingChangeSerializer, MeetingSerializer, \
    MeetingParticipantSerializer
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
    queryset = Group.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return GroupChangeSerializer
        return GroupSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserGroupView(ListAPIView):
    serializer_class = GroupParticipantSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['pk']
        return GroupParticipant.objects.filter(user_id=user_id).order_by("-id")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GroupParticipantSerializer(queryset, many=True)
        for data in serializer.data:
            group_id = data.get("group", None)
            group = get_object_or_404(Group, id=group_id)
            data["group_info"] = {"title": group.title, "city": group.city}
        return Response(serializer.data)


class MeetingViewSet(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MeetingChangeSerializer
        return MeetingSerializer


class UserMeetingView(ListAPIView):
    serializer_class = MeetingParticipantSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['pk']
        return MeetingParticipant.objects.filter(user_id=user_id).order_by("-id")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MeetingParticipantSerializer(queryset, many=True)
        meetings = Meeting.objects.all()
        if self.request.query_params.get('date', None):
            meetings = Meeting.objects.filter(date__gte=datetime.now())

        for data in serializer.data:
            meeting = meetings.filter(id=data.get("meeting", None))
            if meeting:
                data["meeting_info"] = {
                    "title": meeting[0].title,
                    "date": meeting[0].date,
                    "is_online": meeting[0].is_online
                }
        return Response(serializer.data)
