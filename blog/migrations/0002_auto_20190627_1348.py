# Generated by Django 2.2.2 on 2019-06-27 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_creted',
            new_name='date_created',
        ),
    ]