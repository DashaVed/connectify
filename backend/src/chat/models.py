from django.db import models

from web.models import User


class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=False, blank=True)
    room = models.CharField(null=False, blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "чат"
        verbose_name_plural = "чаты"
