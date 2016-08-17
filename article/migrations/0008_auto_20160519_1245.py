# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20160519_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_username',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_username',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
