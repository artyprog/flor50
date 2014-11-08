# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_remove_photo_is_gallerie_bouquet'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='is_gallerie_bouquets',
            field=models.BooleanField(verbose_name='Gallerie des bouquets', default=True),
            preserve_default=True,
        ),
    ]
