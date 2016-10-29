import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'try.settings')
from django.db import models

# Create your models here

class per(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=40)
    summary = models.TextField()
