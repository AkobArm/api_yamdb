# Generated by Django 3.2 on 2023-03-16 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0003_alter_title_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="title",
            options={"ordering": ("name",), "verbose_name": "Произведение"},
        ),
        migrations.AlterField(
            model_name="title",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="titles",
                to="reviews.category",
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="genre",
            field=models.ManyToManyField(
                blank=True,
                related_name="titles",
                to="reviews.Genre",
                verbose_name="Жанр",
            ),
        ),
    ]
