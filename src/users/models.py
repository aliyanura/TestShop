from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from src.common.models import BaseModel
from src.users.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=150, unique=True,
                                verbose_name=("Логин"))
    email = models.EmailField(unique=True, verbose_name='email address')
    password = models.CharField(max_length=128, blank=True,
                                null=True, verbose_name=("Пароль"))
    full_name = models.CharField(max_length=350, null=True, blank=True,
                                 verbose_name='ФИО')
    is_active = models.BooleanField(default=True,
                                    verbose_name=("Является активным"))
    is_staff = models.BooleanField(
        default=False, verbose_name=("Является сотрудником системы")
    )
    is_superuser = models.BooleanField(
        default=False, verbose_name=("Является администратором системы")
    )

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-created_at",)