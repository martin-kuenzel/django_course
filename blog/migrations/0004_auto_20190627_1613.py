# Generated by Django 2.2.2 on 2019-06-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
    ]