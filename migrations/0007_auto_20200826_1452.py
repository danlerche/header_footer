# Generated by Django 3.0.8 on 2020-08-26 21:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0006_auto_20200826_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 14, 52, 55, 954736)),
        ),
    ]