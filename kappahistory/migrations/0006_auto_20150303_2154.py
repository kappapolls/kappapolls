# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kappahistory', '0005_kappasponsorship_drives'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='name',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
