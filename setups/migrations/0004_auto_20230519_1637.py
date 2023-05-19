# Generated by Django 3.2.19 on 2023-05-19 15:37

import cloudinary.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0003_auto_20230519_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='post_action_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_action_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_action_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_bridge_pu_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_bridge_radius',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_fret_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_fret_width',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_fretboard_radius',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_image_1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_image_3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_middle_pu_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_neck_pu_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_neck_relief',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_1_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_2_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_3_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_4_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_5_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_6_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_7_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='post_string_type',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_action_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_action_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_action_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_bridge_pu_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_bridge_radius',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_fret_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_fret_width',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_fretboard_radius',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_image_1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_image_3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_middle_pu_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_neck_pu_height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_neck_relief',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_1_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_2_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_3_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_4_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_5_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_6_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_7_gauge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='pre_string_type',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 15, 37, 0, 710907, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='setup',
            name='datetime_out',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 15, 37, 0, 710924, tzinfo=utc)),
        ),
    ]
