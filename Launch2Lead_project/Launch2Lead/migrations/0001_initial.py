# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Title', models.CharField(unique=True, max_length=128)),
                ('Description', models.CharField(unique=True, max_length=10000)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
            ],
        ),
    ]
