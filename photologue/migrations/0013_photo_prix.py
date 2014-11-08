# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0012_photo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='prix',
            field=models.CharField(verbose_name='prix', max_length=6, default=''),
            preserve_default=True,
        ),
    ]
