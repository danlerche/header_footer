# Generated by Django 3.0.8 on 2020-08-28 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0013_auto_20200827_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]