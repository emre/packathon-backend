# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-16 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
    ]
