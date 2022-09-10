from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from api_yamdb.settings import MSG_FOR_RESERVED_NAME


class UserManager(UserManager):

    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле email обязательное')
        if len(username) < 3:
            raise ValueError(MSG_FOR_RESERVED_NAME)
        return super().create_user(
            username, email=email, password=password, **extra_fields)

    def create_superuser(
            self, username, email, password, role='admin', **extra_fields):
        return super().create_superuser(
            username, email, password, role='admin', **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    username = models.CharField(db_index=True, max_length=150, unique=True)
    role = models.TextField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        max_length=3000,
    )
    objects = UserManager()
    REQUIRED_FIELDS = ['email']

    @property
    def is_admin(self):
        return self.role == self.ROLE_CHOICES[2][0]

    @property
    def is_moderator(self):
        return self.role == self.ROLE_CHOICES[1][0]
