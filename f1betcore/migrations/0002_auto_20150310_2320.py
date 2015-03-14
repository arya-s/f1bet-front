# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1betcore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='points',
            field=models.TextField(default=b'[]'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reddituser',
            name='points',
            field=models.TextField(default=b'[]'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='points',
            field=models.TextField(default=b'[]'),
            preserve_default=True,
        ),
    ]
