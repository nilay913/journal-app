

# Create your models here.
from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField(max_length=200)
    software = models.CharField(max_length=30)
    attachment = models.FileField(upload_to=None, max_length=100)



