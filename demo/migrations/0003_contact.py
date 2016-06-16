# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20160211_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_phone', models.CharField(max_length=20)),
                ('twitter', models.CharField(max_length=20)),
                ('address', models.TextField(null=True, blank=True)),
                ('person', models.ForeignKey(to='demo.Person')),
            ],
        ),
    ]
