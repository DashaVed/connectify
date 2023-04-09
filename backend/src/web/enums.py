from django.db import models


class UserRole(models.TextChoices):
    admin = "admin", "Администратор"
    staff = "staff", "Сотрудник"
    user = "user", "Пользователь"


class ParticipantRole(models.TextChoices):
    admin = 'admin', 'Администратор'
    participant = 'participant', 'Участник'
