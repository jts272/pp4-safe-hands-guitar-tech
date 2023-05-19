# Generated by Django 3.2.19 on 2023-05-19 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='datetime_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 14, 50, 34, 657675, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_out',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 14, 50, 34, 657689, tzinfo=utc)),
        ),
    ]