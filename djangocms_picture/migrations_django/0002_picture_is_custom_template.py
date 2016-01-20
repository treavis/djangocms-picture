# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='is_custom_template',
            field=models.BooleanField(default=False, verbose_name='Template'),
            preserve_default=True,
        ),
    ]
