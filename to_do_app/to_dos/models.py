from datetime import datetime
from unicodedata import category
from django.db import models

# Create your models here.


class To_Do(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, default=datetime.now())

    def __str__(self):
        return self.name
