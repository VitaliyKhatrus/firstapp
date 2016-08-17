# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20160519_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=b'', blank=True),
        ),
    ]
