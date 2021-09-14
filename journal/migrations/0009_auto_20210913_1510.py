# Generated by Django 3.2.7 on 2021-09-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_software'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='software',
        ),
        migrations.AddField(
            model_name='resource',
            name='software',
            field=models.ManyToManyField(to='journal.Software'),
        ),
    ]