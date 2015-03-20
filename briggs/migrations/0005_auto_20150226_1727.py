# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briggs', '0004_briggsquote_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='briggsquote',
            name='visible',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
