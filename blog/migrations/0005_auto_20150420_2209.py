# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150420_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='cnumber',
            field=models.IntegerField(default=0),
        ),
    ]
