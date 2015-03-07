# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kappahistory', '0002_auto_20150302_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='kappasponsorship',
            name='drive',
            field=models.ForeignKey(default=1, to='kappahistory.Drive'),
            preserve_default=False,
        ),
    ]
