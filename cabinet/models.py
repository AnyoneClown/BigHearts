import os
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify


def image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance)}-{uuid.uuid4()}{extension}"
    return os.path.join("uploads/posts/", filename)


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = "New"
        ACTIVE = "Active"
        REJECTED = "Rejected"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
    postType = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to=image_file_path, null=True)
    link = models.URLField(blank=True, null=True)

    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    telegram = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    services = models.ManyToManyField(Service, related_name="posts")
    delivery = models.ManyToManyField(Delivery, related_name="posts")

    class Meta:
        ordering = ["user"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        app_label = "cabinet"
        db_table = "posts"

    def __str__(self):
        return self.title