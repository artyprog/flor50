# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20141015_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
    ]
