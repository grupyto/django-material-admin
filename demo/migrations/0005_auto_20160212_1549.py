# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_person_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter', models.CharField(max_length=50, null=True, blank=True)),
                ('facebook', models.CharField(max_length=50, null=True, blank=True)),
                ('google_plus', models.CharField(max_length=100, null=True, blank=True)),
                ('person', models.ForeignKey(to='demo.Person')),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='twitter',
        ),
    ]
