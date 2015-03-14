# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1betcore', '0003_drivershort'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='number',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
