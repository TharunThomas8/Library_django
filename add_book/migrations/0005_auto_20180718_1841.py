# Generated by Django 2.0.7 on 2018-07-18 18:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('add_book', '0004_auto_20180718_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 18, 18, 41, 39, 334788, tzinfo=utc)),
        ),
    ]
