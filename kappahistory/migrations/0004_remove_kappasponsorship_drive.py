# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kappahistory', '0003_kappasponsorship_drive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kappasponsorship',
            name='drive',
        ),
    ]
