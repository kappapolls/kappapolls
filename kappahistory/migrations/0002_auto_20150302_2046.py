# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kappahistory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='city',
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(default=1, to='kappahistory.Location'),
            preserve_default=False,
        ),
    ]
