# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kappahistory', '0004_remove_kappasponsorship_drive'),
    ]

    operations = [
        migrations.AddField(
            model_name='kappasponsorship',
            name='drives',
            field=models.ManyToManyField(to='kappahistory.Drive', null=True, blank=True),
            preserve_default=True,
        ),
    ]
