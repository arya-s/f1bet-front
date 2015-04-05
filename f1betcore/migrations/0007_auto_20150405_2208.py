# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1betcore', '0006_auto_20150328_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reddituser',
            old_name='updated_at',
            new_name='last_active',
        ),
    ]
