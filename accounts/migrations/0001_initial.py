# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'A/C Name')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('balance', models.FloatField(verbose_name=b'Balance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.CharField(max_length=200, verbose_name=b'Notes')),
                ('debit', models.FloatField(verbose_name=b'Debit Amount')),
                ('credit', models.FloatField(verbose_name=b'Credit Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
