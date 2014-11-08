# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0004_auto_20140915_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='is_couve',
            field=models.BooleanField(verbose_name='Couverture', default=False),
            preserve_default=True,
        ),
    ]
