from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from web.models import User


def get_recipient_lists(participants, is_email=True):
    to_emails = []
    for participant in participants:
        if is_email:
            to_emails.append(participant.user.email)
        else:
            user = get_object_or_404(User, id=participant["fields"]["user"])
            to_emails.append(user.email)
    return to_emails


def send_email(template_name, subject, contex, to_emails):
    html_content = get_template(template_name).render(contex)
    msg = EmailMultiAlternatives(subject, '', 'dasha.test93@gmail.com', to_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
