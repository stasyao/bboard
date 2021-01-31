import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
# для интернационализации
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """Кастомная модель пользователя доски объявлений"""
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'пользователь'),
        (MODERATOR, 'модератор'),
        (ADMIN, 'администратор'),
    )
    username = None
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('имя'),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('фамилия'),
    )
    middle_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('отчество'),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name=_('роль'),
    )
    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name='email' # Не локализуем, общепринятое в мире обозначение
    )
    phone_number = models.CharField(
        max_length=10,
        blank=False,
        unique=True,
        verbose_name=_('телефонный номер'),
    )
    call_reception_time = models.CharField(
        max_length=255,
        verbose_name=_('Удобное время приема звонков'),
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name=_('Статус активации'),
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.email
