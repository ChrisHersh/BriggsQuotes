# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briggs', '0002_auto_20150223_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='briggsquote',
            old_name='votes',
            new_name='votesNeg',
        ),
        migrations.AddField(
            model_name='briggsquote',
            name='votesPos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
