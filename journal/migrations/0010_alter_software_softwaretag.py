# Generated by Django 3.2.7 on 2021-09-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_auto_20210913_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='SoftwareTag',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]