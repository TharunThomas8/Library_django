# Generated by Django 2.0.7 on 2018-07-23 21:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('add_book', '0014_auto_20180723_2128'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='examplelist',
            new_name='massfile',
        ),
        migrations.AlterField(
            model_name='booklist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 23, 21, 32, 36, 931851, tzinfo=utc)),
        ),
    ]
