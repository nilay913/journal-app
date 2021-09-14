from django.contrib import admin

# Register your models here.
from .models import Resource
from .models import Software

admin.site.register(Resource)
admin.site.register(Software)