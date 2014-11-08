# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0006_auto_20140929_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='is_gallerie_bouquet',
            field=models.BooleanField(default=True, verbose_name='Gallerie des Bouquets'),
            preserve_default=True,
        ),
    ]
