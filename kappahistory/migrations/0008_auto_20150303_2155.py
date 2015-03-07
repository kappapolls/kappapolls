# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kappahistory', '0007_auto_20150303_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drive',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
