# Generated by Django 3.0.8 on 2020-08-26 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0005_auto_20200826_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 14, 48, 21, 688144)),
        ),
    ]