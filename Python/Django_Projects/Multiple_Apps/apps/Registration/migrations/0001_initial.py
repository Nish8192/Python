# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Register_Login', '0003_auto_20170221_1754'),
        ('Course_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='Course_App.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='Register_Login.User')),
            ],
        ),
    ]