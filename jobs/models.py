from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    skill = models.CharField(max_length=200)
    source = models.CharField(max_length=50, default="cakeresume")

    def __str__(self):
        return self.title