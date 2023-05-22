import json

from django.shortcuts import get_object_or_404

from main.celery import app
from web.models import Meeting, GroupParticipant, MeetingParticipant
from web.sevices import get_recipient_lists, send_email


@app.task
def send_create_meeting_email(meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    to_emails = get_recipient_lists(GroupParticipant.objects.filter(group=meeting.group.id, role='participant'))
    if to_emails:
        subject = f'Новая встреча в группе {meeting.group.title}'
        send_email(template_name='emails/meeting_create_email.html', subject=subject,
                   contex={'meeting': meeting}, to_emails=to_emails)
        print('email sent')


@app.task
def send_delete_meeting_email(meeting, meeting_participants):
    meeting = json.loads(meeting)[0]
    meeting_participants = json.loads(meeting_participants)
    to_emails = get_recipient_lists(meeting_participants, is_email=False)
    print(to_emails)
    if to_emails:
        subject = f'Отменили встречу: {meeting["fields"]["title"]}'
        send_email(template_name='emails/meeting_delete_email.html', subject=subject,
                   contex={'meeting': meeting["fields"]}, to_emails=to_emails)



@app.task
def send_delete_group_email(group_title):
    pass
