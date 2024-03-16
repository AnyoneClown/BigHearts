# Generated by Django 5.0.2 on 2024-03-12 07:06

import cabinet.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Delivery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("postType", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=100)),
                ("text", models.TextField()),
                (
                    "image",
                    models.ImageField(null=True, upload_to=cabinet.models.image_file_path),
                ),
                ("link", models.URLField(blank=True, null=True)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("telegram", models.CharField(blank=True, max_length=100, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("New", "New"),
                            ("Active", "Active"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "delivery",
                    models.ManyToManyField(related_name="posts", to="cabinet.delivery"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "services",
                    models.ManyToManyField(related_name="posts", to="cabinet.service"),
                ),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
                "db_table": "posts",
                "ordering": ["user"],
            },
        ),
    ]
