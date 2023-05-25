from datetime import datetime
from rest_framework.generics import UpdateAPIView, ListAPIView, get_object_or_404, DestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer, GroupChangeSerializer, ChangePasswordSerializer, \
    CategorySerializer, GroupParticipantSerializer, MeetingChangeSerializer, MeetingSerializer, \
    MeetingParticipantSerializer
from web.models import User, Group, Category, GroupParticipant, Meeting, MeetingParticipant
from web.services import get_meeting_data_for_email, get_group_data_for_email
from web.tasks import send_create_meeting_email, send_delete_meeting_email, send_delete_group_email


class EnablePartialUpdateMixin:

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class UserViewSet(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class GroupViewSet(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return GroupChangeSerializer
        return GroupSerializer

    def destroy(self, request, *args, **kwargs):
        group_str, group_participant_str = get_group_data_for_email(self.request.parser_context['kwargs']['pk'])
        send_delete_group_email.delay(group_str, group_participant_str)
        return super().destroy(request, *args, **kwargs)


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserGroupView(ListAPIView):
    serializer_class = GroupParticipantSerializer
    permission_classes = [IsAuthenticated]

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

    def get_queryset(self):
        meetings = Meeting.objects.all()
        if self.action == 'list':
            meetings = Meeting.objects.filter(date__gte=datetime.now()).order_by("-created_at")
            group_id = self.request.query_params.get("group", None)
            if group_id:
                meetings = Meeting.objects.filter(group_id=group_id)
        return meetings

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MeetingChangeSerializer
        return MeetingSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            send_create_meeting_email.delay(response.data['id'])
        return response

    def destroy(self, request, *args, **kwargs):
        meeting_str, meeting_participant_str = get_meeting_data_for_email(self.request.parser_context['kwargs']['pk'])
        send_delete_meeting_email.delay(meeting_str, meeting_participant_str)
        return super().destroy(request, *args, **kwargs)


class UserMeetingView(ListAPIView):
    serializer_class = MeetingParticipantSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['pk']
        return MeetingParticipant.objects.filter(user_id=user_id).order_by("-id")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MeetingParticipantSerializer(queryset, many=True)
        meetings = Meeting.objects.filter(date__gte=datetime.now())
        for data in serializer.data:
            meeting = meetings.filter(id=data.get("meeting", None))
            if meeting:
                data["meeting_info"] = {
                    "title": meeting[0].title,
                    "date": meeting[0].date,
                    "is_online": meeting[0].is_online
                }
                if meeting[0].location:
                    data["meeting_info"]["location"] = meeting[0].location
                else:
                    data["meeting_info"]["location"] = ""
        return Response(serializer.data)


class DeleteGroupParticipantView(DestroyAPIView):
    serializer_class = GroupParticipantSerializer
    queryset = GroupParticipant.objects.all()


class DeleteMeetingParticipantView(DestroyAPIView):
    serializer_class = MeetingParticipantSerializer
    queryset = MeetingParticipant.objects.all()
