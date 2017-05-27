# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h9to10', models.BooleanField(verbose_name=False)),
                ('h10to11', models.BooleanField(verbose_name=False)),
                ('h11to12', models.BooleanField(verbose_name=False)),
                ('h12to13', models.BooleanField(verbose_name=False)),
                ('h13to14', models.BooleanField(verbose_name=False)),
                ('h14to15', models.BooleanField(verbose_name=False)),
                ('h15to16', models.BooleanField(verbose_name=False)),
                ('h16to17', models.BooleanField(verbose_name=False)),
                ('h17to18', models.BooleanField(verbose_name=False)),
                ('h18to19', models.BooleanField(verbose_name=False)),
                ('h19to20', models.BooleanField(verbose_name=False)),
                ('h20to21', models.BooleanField(verbose_name=False)),
                ('h21to22', models.BooleanField(verbose_name=False)),
                ('h22to23', models.BooleanField(verbose_name=False)),
                ('h23to0', models.BooleanField(verbose_name=False)),
                ('h0to1', models.BooleanField(verbose_name=False)),
                ('h1to2', models.BooleanField(verbose_name=False)),
                ('h2to3', models.BooleanField(verbose_name=False)),
                ('h3to4', models.BooleanField(verbose_name=False)),
                ('h4to5', models.BooleanField(verbose_name=False)),
                ('h5to6', models.BooleanField(verbose_name=False)),
                ('h6to7', models.BooleanField(verbose_name=False)),
                ('h7to8', models.BooleanField(verbose_name=False)),
                ('h8to9', models.BooleanField(verbose_name=False)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri_schedule', to='schedules.Day')),
                ('mon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mon_schedule', to='schedules.Day')),
                ('sat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sat_schedule', to='schedules.Day')),
                ('sun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sun_schedule', to='schedules.Day')),
                ('thu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thu_schedule', to='schedules.Day')),
                ('tue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tue_schedule', to='schedules.Day')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_user', to='login_register.User')),
                ('wed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wed_schedule', to='schedules.Day')),
            ],
        ),
    ]
