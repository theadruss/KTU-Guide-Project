# Generated by Django 5.1.2 on 2024-10-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ktuguideapp', '0002_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='sem_number',
            field=models.IntegerField(default=1),
        ),
    ]
