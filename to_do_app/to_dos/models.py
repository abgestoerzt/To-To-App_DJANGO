from unicodedata import category
from django.db import models

# Create your models here.


class To_Do(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    category = models.CharField(max_length=255)
