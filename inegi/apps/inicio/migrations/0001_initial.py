# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('idEquipo', models.AutoField(serialize=False, primary_key=True)),
                ('nombreEquipo', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('clavefile', models.AutoField(serialize=False, primary_key=True)),
                ('docfile', models.FileField(upload_to='equipos')),
                ('idEquipo', models.ForeignKey(to='inicio.Equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parche',
            fields=[
                ('IdParche', models.AutoField(serialize=False, primary_key=True)),
                ('nombreParche', models.CharField(max_length=50)),
                ('ParcheFecha', models.CharField(max_length=50)),
                ('fechaAviso', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('fechaInstalacion', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SistemaOperativo',
            fields=[
                ('idSo', models.AutoField(serialize=False, primary_key=True)),
                ('nombreSistema', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='parche',
            name='sistema',
            field=models.ForeignKey(to='inicio.SistemaOperativo'),
            preserve_default=True,
        ),
    ]
