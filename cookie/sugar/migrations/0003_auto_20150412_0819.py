# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sugar', '0002_auto_20150412_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='days_since_served',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='last_day_served',
            field=models.DateTimeField(null=True),
        ),
    ]
