# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briggs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BriggsVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('quote', models.ForeignKey(to='briggs.BriggsQuote')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='briggsvotes',
            name='quote',
        ),
        migrations.DeleteModel(
            name='BriggsVotes',
        ),
    ]
