# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150419_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ment', models.TextField()),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
