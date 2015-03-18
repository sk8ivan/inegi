# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='docfile',
            field=models.FileField(upload_to='Windows'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='update',
            name='docUpdate',
            field=models.FileField(upload_to='Update'),
            preserve_default=True,
        ),
    ]
