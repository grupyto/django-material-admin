# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.FileField(null=True, upload_to=b'person', blank=True),
        ),
    ]
