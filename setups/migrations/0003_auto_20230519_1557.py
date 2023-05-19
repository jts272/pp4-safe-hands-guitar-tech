# Generated by Django 3.2.19 on 2023-05-19 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0002_auto_20230519_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='name',
            field=models.CharField(default='Guitar name', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 14, 57, 23, 414301, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_out',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 14, 57, 23, 414316, tzinfo=utc)),
        ),
    ]
