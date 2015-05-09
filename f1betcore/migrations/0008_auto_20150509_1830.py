# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1betcore', '0007_auto_20150405_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reddituser',
            name='last_active',
        ),
        migrations.AlterField(
            model_name='bet',
            name='timestamp',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
