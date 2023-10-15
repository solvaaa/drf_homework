from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = ('member', 'пользователь')
    MODERATOR = ('moderator', 'модератор')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=30, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=12, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
