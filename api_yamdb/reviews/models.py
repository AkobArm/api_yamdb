from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

SIM_NUMB: int = 15


class Category(models.Model):
    """Модель категории произведения"""

    name = models.CharField(max_length=200, verbose_name="категория произведения")
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория"

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанра произведения"""

    name = models.CharField(max_length=200, verbose_name="жанр произведения")
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Жанр"

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведения"""

    name = models.CharField(max_length=200, verbose_name="название произведения")
    description = models.TextField(max_length=250, verbose_name="описание", blank=True)
    year = models.IntegerField(verbose_name="год выпуска произведения")
    genre = models.ManyToManyField(
        Genre, blank=True, related_name="titles", verbose_name="Жанр"
    )
    category = models.ForeignKey(
        Category,
        related_name="titles",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Произведение"

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Связывающая модель"""

    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["title", "genre"], name="GenreTitle"),
        ]

    def __str__(self):
        return f"Произведение:{self.title} жанр: {self.genre}"


class Review(models.Model):
    """Модель отзыва"""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    score = models.IntegerField(
        "Оценка",
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10),
        ),
    )
    pub_date = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "title",
                    "author",
                ),
                name="unique review",
            )
        ]
        ordering = ("pub_date",)

    def __str__(self):
        return self.text[:SIM_NUMB]


class Comment(models.Model):
    """Модель комментария"""

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.CharField("Текст комментария", max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text[:SIM_NUMB]
