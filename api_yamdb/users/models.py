from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = (
    ('user', 'User'),
    ('moderator', 'Moderator'),
    ('admin', 'Admin'),
)


class User(AbstractUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default='user',
    )

    class Meta:
        ordering = ['-id']

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'
