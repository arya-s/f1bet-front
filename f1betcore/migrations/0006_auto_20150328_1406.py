# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1betcore', '0005_auto_20150311_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reddituser',
            old_name='last_active',
            new_name='updated_at',
        ),
    ]
