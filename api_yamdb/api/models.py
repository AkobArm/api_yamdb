from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    username = models.CharField(max_length=200,
                                verbose_name='логин юзера')
    email = models.EmailField(max_length=200,
                              unique=True)
    first_name = models.CharField(max_length=200,
                                  verbose_name='имя юзера')
    last_name = models.CharField(max_length=200,
                                 verbose_name='фамилия юзера')
    password = models.CharField(max_length=200,
                                blank=True)

    def __str__(self):
        return self.username


class Title(models.Model):
    """Модель произведения"""
    name = models.CharField(max_length=200,
                            verbose_name='название произведения')
    description = models.CharField(max_length=250,
                                   verbose_name='описание',
                                   blank=True)
    year = models.IntegerField(verbose_name='год выпуска произведения')

    class Meta:
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель категории произведения"""
    name = models.CharField(max_length=200,
                            verbose_name='категория произведения',
                            unique=True)
    slug = models.SlugField(max_length=50,
                            unique=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанра произведения"""
    name = models.CharField(max_length=200,
                            verbose_name='жанр произведения',
                            unique=True)
    slug = models.SlugField(max_length=50,
                            unique=True)

    class Meta:
        verbose_name = 'Жанр'

    def __str__(self):
        return self.name
