# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='permissions',
            field=models.ManyToManyField(to='demo.Permissions'),
        ),
    ]
