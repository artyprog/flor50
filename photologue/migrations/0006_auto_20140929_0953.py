# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0005_gallery_is_couve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='is_couve',
        ),
        migrations.AddField(
            model_name='photo',
            name='is_cover',
            field=models.BooleanField(verbose_name="Couverture de l'album", default=False),
            preserve_default=True,
        ),
    ]
