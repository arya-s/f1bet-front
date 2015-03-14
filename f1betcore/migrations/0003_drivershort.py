# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1betcore', '0002_auto_20150310_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverShort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tlid', models.TextField(null=True)),
                ('driver', models.ForeignKey(to='f1betcore.Driver')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
