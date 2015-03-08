# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_choice_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kappauser',
            name='username',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poll',
            name='name',
            field=models.CharField(unique=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poll',
            name='thread_id',
            field=models.CharField(unique=True, max_length=256),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'choice')]),
        ),
    ]
