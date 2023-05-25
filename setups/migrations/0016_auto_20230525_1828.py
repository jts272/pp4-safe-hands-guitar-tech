# Generated by Django 3.2.19 on 2023-05-25 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0015_auto_20230525_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_in',
            field=models.DateField(blank=True, default=datetime.datetime.now, help_text='Date format is YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_out',
            field=models.DateField(blank=True, default=datetime.datetime.now, help_text='Date format is YYYY-MM-DD', null=True),
        ),
    ]
