# Generated by Django 2.2.2 on 2019-06-30 00:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
