# Generated by Django 4.2.6 on 2023-11-05 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_remove_user_is_contributor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 7, 30, 9, 197318, tzinfo=datetime.timezone.utc)),
        ),
    ]
