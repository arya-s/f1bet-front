# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dbarray.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('points', dbarray.fields.FloatArrayField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('finished', models.BooleanField(default=False)),
                ('driver_list', models.ManyToManyField(to='f1betcore.Driver')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RedditUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('flair', models.TextField(null=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('points', dbarray.fields.FloatArrayField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('points', dbarray.fields.FloatArrayField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='driver',
            name='team',
            field=models.ForeignKey(to='f1betcore.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bet',
            name='drivers',
            field=models.ManyToManyField(to='f1betcore.Driver'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bet',
            name='race',
            field=models.ForeignKey(to='f1betcore.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(to='f1betcore.RedditUser'),
            preserve_default=True,
        ),
    ]
