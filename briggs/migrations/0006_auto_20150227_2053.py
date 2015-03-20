# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briggs', '0005_auto_20150226_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='briggsquote',
            name='visible',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
