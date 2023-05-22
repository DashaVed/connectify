import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object("django.conf:settings", namespace='CELERY')

app.conf.beat_schedule = {
    'send_mail': {
        'task': 'web.tasks.send_notification_email',
        'schedule': crontab(hour=8, minute=0),
    }
}

app.autodiscover_tasks()
