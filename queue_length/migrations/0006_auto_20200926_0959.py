# Generated by Django 3.1.1 on 2020-09-26 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queue_length', '0005_auto_20200926_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queue',
            old_name='date_time_get',
            new_name='updated_time',
        ),
    ]
