# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.text import slugify

def gen_slug(apps, schema_editor):
    Poll = apps.get_model('polls', 'Poll')
    for row in Poll.objects.all():
        row.slug = slugify(row.name)
        row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150301_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='slug',
            field=models.SlugField(max_length=500, null=True),
            preserve_default=False,
        ),
        migrations.RunPython(gen_slug,),
        migrations.AlterField(
            model_name='poll',
            name='slug',
            field=models.SlugField(default='myslug', unique=True)
            ),
    ]
