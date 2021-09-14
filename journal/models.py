# Create your models here.
from django.db import models

class Software(models.Model):
    SoftwareTag = models.CharField(max_length=50)
    def __str__(self):
        return self.SoftwareTag

class Resource(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField(max_length=200, blank=True, null=True)
    software = models.ManyToManyField(Software)
    attachment = models.FileField(upload_to=".", max_length=100, blank=True, null=True)