# Generated by Django 4.0.6 on 2022-09-20 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_dos', '0009_alter_to_do_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 20, 15, 27, 0, 889927)),
        ),
    ]