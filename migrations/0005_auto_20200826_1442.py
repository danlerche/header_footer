# Generated by Django 3.0.8 on 2020-08-26 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0004_auto_20200825_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_colour',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green')], default='G', max_length=1),
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 14, 42, 9, 183810)),
        ),
    ]
