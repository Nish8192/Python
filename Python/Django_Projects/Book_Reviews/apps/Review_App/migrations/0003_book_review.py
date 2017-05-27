# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Review_App', '0002_user_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('stars', models.CharField(max_length=1)),
                ('book_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_book', to='Review_App.Book')),
                ('user_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to='Review_App.User')),
            ],
        ),
    ]
