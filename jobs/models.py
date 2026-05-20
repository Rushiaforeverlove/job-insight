from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    salary = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    skill = models.CharField(max_length=200)


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )