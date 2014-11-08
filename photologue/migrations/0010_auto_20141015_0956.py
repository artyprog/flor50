# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0009_gallery_is_gallerie_bouquets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
            preserve_default=False,
        ),
    ]
