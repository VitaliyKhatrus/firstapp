# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20151022_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-article_date',)},
        ),
        migrations.AddField(
            model_name='article',
            name='article_dislikes',
            field=models.IntegerField(default=0),
        ),
    ]
