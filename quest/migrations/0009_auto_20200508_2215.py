# Generated by Django 2.2.11 on 2020-05-08 16:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0008_auto_20200508_2207'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SolutionCallBack',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 16, 45, 35, 438797, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 16, 45, 35, 438797, tzinfo=utc)),
        ),
    ]
