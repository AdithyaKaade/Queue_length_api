# Generated by Django 3.1.1 on 2020-09-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_length', '0003_auto_20200926_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='queue_length',
            field=models.IntegerField(),
        ),
    ]