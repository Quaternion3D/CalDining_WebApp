# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sugar', '0004_remove_food_days_since_served'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favs',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='last_day_served',
            field=models.DateTimeField(),
        ),
    ]
