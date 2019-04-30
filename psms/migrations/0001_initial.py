# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'ywx',
            },
        ),
        migrations.CreateModel(
            name='service_summary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yew', models.CharField(max_length=10)),
                ('y_url', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'zywx',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_name', models.CharField(max_length=10)),
                ('u_password', models.CharField(max_length=255)),
                ('u_ticket', models.CharField(max_length=30, null=True)),
                ('u_icon', models.ImageField(default=b'icon/default.png', upload_to=b'icon')),
                ('is_active', models.BooleanField(default=False)),
                ('favor', models.ManyToManyField(to='psms.Service_line')),
            ],
            options={
                'db_table': 'zcdl',
            },
        ),
        migrations.AlterUniqueTogether(
            name='users',
            unique_together=set([('u_name',)]),
        ),
    ]
