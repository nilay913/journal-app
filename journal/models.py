

# Create your models here.
from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField(max_length=200, blank=True, null=True)
    software = models.CharField(max_length=30, blank=True, null=True)
    attachment = models.FileField(upload_to="media/", max_length=100, blank=True, null=True)



