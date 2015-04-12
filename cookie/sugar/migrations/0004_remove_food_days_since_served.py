# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sugar', '0003_auto_20150412_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='days_since_served',
        ),
    ]
