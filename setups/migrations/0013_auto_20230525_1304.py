# Generated by Django 3.2.19 on 2023-05-25 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0012_auto_20230524_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='post_strings',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pre_strings',
        ),
        migrations.AddField(
            model_name='job',
            name='post_action_1',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_action_2',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_action_3',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_bridge_pickup_height',
            field=models.CharField(blank=True, help_text='Provide values for polepiece height on bass and treble side, with the last fret fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_bridge_saddle_radius',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_fret_width_and_height',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_fretboard_radius',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_middle_pickup_height',
            field=models.CharField(blank=True, help_text='Provide values for polepiece height on bass and treble side, with the last fret fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_neck_pickup_height',
            field=models.CharField(blank=True, help_text='Provide values for polepiece height on bass and treble side, with the last fret fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_neck_relief',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_nut_action',
            field=models.CharField(blank=True, help_text='Specify if the reading is open or fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_scale_length',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_string_brand',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='post_string_gauges',
            field=models.CharField(blank=True, help_text='Provide either the gauge of the set, e.g. 10-52 or each  individual string, from first string to last string', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_action_1',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_action_2',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_action_3',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_bridge_pickup_height',
            field=models.CharField(blank=True, help_text='Provide values for polepiece height on bass and treble side, with the last fret fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_bridge_saddle_radius',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_fret_width_and_height',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_fretboard_radius',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_middle_pickup_height',
            field=models.CharField(blank=True, help_text='Provide values for polepiece height on bass and treble side, with the last fret fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_neck_pickup_height',
            field=models.CharField(blank=True, help_text='Provide values for polepiece height on bass and treble side, with the last fret fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_neck_relief',
            field=models.CharField(blank=True, help_text='Specify at which fret the measurement was taken', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_nut_action',
            field=models.CharField(blank=True, help_text='Specify if the reading is open or fretted', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_scale_length',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_string_brand',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pre_string_gauges',
            field=models.CharField(blank=True, help_text='Provide either the gauge of the set, e.g. 10-52 or each  individual string, from first string to last string', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='instrument',
            field=models.CharField(default='Unnamed instrument', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 11, 54, 28, 579598, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_out',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 11, 54, 28, 579622, tzinfo=utc)),
        ),
    ]