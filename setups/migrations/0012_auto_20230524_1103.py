# Generated by Django 3.2.19 on 2023-05-24 10:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0011_auto_20230521_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='datetime_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 10, 3, 52, 308325, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_out',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 10, 3, 52, 308354, tzinfo=utc)),
        ),
    ]
