# Generated by Django 2.2.2 on 2019-06-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190630_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='title',
            field=models.CharField(default='Option Title', max_length=200),
        ),
    ]
