# Generated by Django 4.2.6 on 2023-11-12 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0011_alter_passwordresetinfo_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 20, 2, 47, 527753, tzinfo=datetime.timezone.utc)),
        ),
    ]
