# Generated by Django 3.2.19 on 2023-05-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0016_auto_20230525_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='public_status',
            field=models.IntegerField(choices=[(0, 'Hidden'), (1, 'Visible')], default=1),
        ),
    ]
