# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='last_modify_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
