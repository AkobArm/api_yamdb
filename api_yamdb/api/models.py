from django.db import models


class Category(models.Model):
    """Модель категории произведения"""
    name = models.CharField(max_length=200,
                            verbose_name='категория произведения')
    slug = models.SlugField(max_length=50,
                            unique=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанра произведения"""
    name = models.CharField(max_length=200,
                            verbose_name='жанр произведения')
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
                                   blank=True,
                                   null=True)
    rating = models.IntegerField(null=True)
    year = models.IntegerField(verbose_name='год выпуска произведения')
    genre = models.ManyToManyField(Genre,
                                   blank=True,
                                   verbose_name='Жанр')
    category = models.ForeignKey(
        Category, related_name='title', blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Связывающая модель"""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'genre'], name='GenreTitle'
            ),
        ]

    def __str__(self):
        return f'Произведение:{self.title} жанр: {self.genre}'
