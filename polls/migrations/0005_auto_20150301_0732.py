# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150228_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='close_date',
            field=models.DateField(default=datetime.date(2015, 3, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='open_date',
            field=models.DateField(default=datetime.date(2015, 3, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='comment_id',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
