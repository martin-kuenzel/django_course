# Generated by Django 2.2.2 on 2019-06-27 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190627_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]