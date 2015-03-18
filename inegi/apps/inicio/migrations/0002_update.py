# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('claveUpdate', models.AutoField(serialize=False, primary_key=True)),
                ('docUpdate', models.FileField(upload_to='equipos')),
                ('idEquipo', models.ForeignKey(to='inicio.Equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
