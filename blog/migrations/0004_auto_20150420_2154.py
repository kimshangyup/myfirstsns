# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_chat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.AddField(
            model_name='entries',
            name='cnumber',
            field=models.CharField(default=0, max_length=4),
        ),
    ]
