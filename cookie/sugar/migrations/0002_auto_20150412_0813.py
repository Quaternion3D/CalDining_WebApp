# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='days_since_served',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 8, 12, 56, 912947, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='last_day_served',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 8, 13, 3, 562706, tzinfo=utc), verbose_name=datetime.datetime(2015, 4, 12, 8, 12, 45, 842586, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='output',
            field=models.CharField(default=datetime.datetime(2015, 4, 12, 8, 13, 17, 299251, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
    ]
