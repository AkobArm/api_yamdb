from django.contrib.auth.models import AbstractUser
from django.db import models


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


class Title(models.Model):
    """Модель произведения"""
    name = models.CharField(max_length=200,
                            verbose_name='название произведения')
    description = models.CharField(max_length=250,
                                   verbose_name='описание',
                                   blank=True
                                   null=True)
    year = models.IntegerField(verbose_name='год выпуска произведения')
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(
        Category, related_name='title', blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name
