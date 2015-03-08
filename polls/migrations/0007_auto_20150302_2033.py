# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_poll_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='slug',
            field=models.SlugField(unique=True, max_length=500),
            preserve_default=True,
        ),
    ]
