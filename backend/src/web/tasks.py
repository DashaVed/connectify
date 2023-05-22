from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template

from main.celery import app
from web.models import Meeting, GroupParticipant, User


@app.task
def send_create_meeting_email(meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    html_content = get_template('emails/meeting_create_email.html').render({'meeting': meeting})
    group_participants = GroupParticipant.objects.filter(meeting=meeting_id, role='participant')
    to_emails = []
    for gp in group_participants:
        user = get_object_or_404(User, id=gp.user)
        to_emails.append(user.email)

    subject = f'Новая встреча в группе {meeting.group.title}'

    if to_emails:
        msg = EmailMultiAlternatives(subject, '', 'dasha.test93@gmail.com', to_emails)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
