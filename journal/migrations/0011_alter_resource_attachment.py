# Generated by Django 3.2.7 on 2021-09-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0010_alter_software_softwaretag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
