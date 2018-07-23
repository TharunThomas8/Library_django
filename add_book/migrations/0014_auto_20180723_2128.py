# Generated by Django 2.0.7 on 2018-07-23 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('add_book', '0013_auto_20180723_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='examplelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='mass_upload/')),
            ],
        ),
        migrations.AlterField(
            model_name='booklist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 23, 21, 28, 20, 106358, tzinfo=utc)),
        ),
    ]
