# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kappahistory', '0006_auto_20150303_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drive',
            old_name='name',
            new_name='url',
        ),
    ]
