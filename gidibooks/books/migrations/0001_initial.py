# Generated by Django 3.1.7 on 2021-04-06 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(
            settings.AUTH_USER_MODEL
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "book_id",
                    models.UUIDField(default=uuid.uuid4),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200, verbose_name="title"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("borrowed", "borrowed"),
                            ("available", "available"),
                            ("pending", "pending"),
                        ],
                        default="available",
                        max_length=20,
                        verbose_name="book status",
                    ),
                ),
                (
                    "created",
                    models.DateField(auto_now_add=True),
                ),
                (
                    "updated",
                    models.DateField(auto_now=True),
                ),
                (
                    "borrower",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
