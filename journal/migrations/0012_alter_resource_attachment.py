# Generated by Django 3.2.7 on 2021-09-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0011_alter_resource_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='media/media/'),
        ),
    ]