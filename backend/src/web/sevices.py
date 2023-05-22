from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def get_recipient_lists(participants):
    to_emails = []
    for participant in participants:
        to_emails.append(participant.user.email)
    return to_emails


def send_email(template_name, subject, contex, to_emails):
    html_content = get_template(template_name).render(contex)
    msg = EmailMultiAlternatives(subject, '', 'dasha.test93@gmail.com', to_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
