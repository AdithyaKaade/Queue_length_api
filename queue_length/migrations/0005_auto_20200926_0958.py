# Generated by Django 3.1.1 on 2020-09-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_length', '0004_auto_20200926_0910'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logdata_get',
        ),
        migrations.AddField(
            model_name='queue',
            name='date_time_get',
            field=models.DateTimeField(auto_now=True, verbose_name='queue_length'),
        ),
    ]
