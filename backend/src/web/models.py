from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models

from web.enums import UserRole, ParticipantRole


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role=UserRole.admin, **extra_fields)


def upload_to(filename):
    return f'profiles/{filename}'


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(unique=True)
    role = models.CharField(choices=UserRole.choices, max_length=15, default=UserRole.user)
    name = models.CharField(max_length=512, null=True, blank=False, verbose_name='ФИ')
    city = models.CharField(max_length=255, null=True, blank=False, verbose_name='Город проживания')
    gender = models.CharField(max_length=1, null=True, blank=True, verbose_name='Пол')
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True, default='profiles/default_user.png',
                              verbose_name='Фотография')
    is_active = models.BooleanField(default=True)

    @property
    def is_staff(self):
        return self.role in (UserRole.admin, UserRole.staff)

    @property
    def is_superuser(self):
        return self.role == UserRole.admin

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'city']

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Category(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Group(BaseModel):
    title = models.CharField(max_length=500, null=False, blank=False, verbose_name='Название группы')
    city = models.CharField(max_length=255, null=False, blank=False, verbose_name='Город')
    description = models.TextField(verbose_name='Описание')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    users = models.ManyToManyField(User, through='GroupParticipant', verbose_name='Пользователи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группы"


class GroupParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ParticipantRole.choices)

    class Meta:
        unique_together = [['user', 'group']]


class Meeting(BaseModel):
    title = models.CharField(max_length=500, null=False, blank=False, verbose_name='Название встречи')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Место встречи')
    description = models.TextField(verbose_name='Описание')
    is_online = models.BooleanField(default=False)
    date = models.DateTimeField(verbose_name='Дата проведения')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    users = models.ManyToManyField(User, through='MeetingParticipant', verbose_name='Пользователи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "встреча"
        verbose_name_plural = "встречи"


class MeetingParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ParticipantRole.choices)

    class Meta:
        unique_together = [['user', 'meeting']]
