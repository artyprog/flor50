# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0007_photo_is_gallerie_bouquet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='is_gallerie_bouquet',
        ),
    ]
