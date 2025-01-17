# Generated by Django 5.1.2 on 2024-10-20 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KTUUpdates',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('join_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('scheme_id', models.AutoField(primary_key=True, serialize=False)),
                ('scheme_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=100)),
                ('scheme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='ktuguideapp.scheme')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('sem_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='ktuguideapp.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('notes_link', models.URLField()),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='ktuguideapp.semester')),
            ],
        ),
        migrations.CreateModel(
            name='YTLink',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('links', models.URLField()),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yt_links', to='ktuguideapp.semester')),
            ],
        ),
    ]
