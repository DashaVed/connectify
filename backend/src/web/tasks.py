import json

from datetime import datetime, timedelta

from celery.utils.log import get_task_logger
from django.shortcuts import get_object_or_404

from main.celery import app
from web.models import Meeting, GroupParticipant, MeetingParticipant
from web.services import get_recipient_lists, send_email


logger = get_task_logger(__name__)


@app.task
def send_create_meeting_email(meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    to_emails = get_recipient_lists(GroupParticipant.objects.filter(group=meeting.group.id, role='participant'))
    if to_emails:
        subject = f'Новая встреча в группе {meeting.group.title}'
        send_email(template_name='emails/meeting_create_email.html', subject=subject,
                   contex={'meeting': meeting}, to_emails=to_emails)


@app.task
def send_delete_meeting_email(meeting, meeting_participants):
    meeting = json.loads(meeting)[0]
    meeting_participants = json.loads(meeting_participants)
    to_emails = get_recipient_lists(meeting_participants, is_email=False)
    if to_emails:
        subject = f'Отменили встречу: {meeting["fields"]["title"]}'
        send_email(template_name='emails/meeting_delete_email.html', subject=subject,
                   contex={'meeting': meeting["fields"]}, to_emails=to_emails)


@app.task
def send_delete_group_email(group, group_participants):
    group = json.loads(group)[0]
    group_participants = json.loads(group_participants)
    to_emails = get_recipient_lists(group_participants, is_email=False)
    if to_emails:
        subject = f'Администратор удалил группу: {group["fields"]["title"]}'
        send_email(template_name='emails/group_delete_email.html', subject=subject,
                   contex={'group': group["fields"]}, to_emails=to_emails)


@app.task
def send_notification_email():
    next_day = datetime.now().date() + timedelta(days=1)
    start_time = datetime.combine(next_day, datetime.min.time())
    end_time = datetime.combine(next_day, datetime.max.time())
    meetings = Meeting.objects.filter(date__range=(start_time, end_time))
    for meeting in meetings:
        to_emails = get_recipient_lists(MeetingParticipant.objects.filter(meeting=meeting, role="participant"))
        if to_emails:
            subject = f'Не забудьте про встречу в группе {meeting.group.title}'
            send_email(template_name='emails/meeting_notify_email.html', subject=subject,
                       contex={'meeting': meeting}, to_emails=to_emails)

