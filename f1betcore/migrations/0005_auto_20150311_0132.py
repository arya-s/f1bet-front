# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1betcore', '0004_driver_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='name',
            new_name='grand_prix',
        ),
        migrations.AddField(
            model_name='race',
            name='circuit',
            field=models.TextField(default='TBA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='round',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
