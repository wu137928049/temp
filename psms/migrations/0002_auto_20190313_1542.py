# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='favor',
        ),
        migrations.AddField(
            model_name='service_line',
            name='favor',
            field=models.ManyToManyField(to='psms.Users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='u_name',
            field=models.CharField(max_length=5),
        ),
    ]
