# Generated by Django 4.2.6 on 2023-11-14 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_app', '0005_plant_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinalplant',
            name='is_medicinal',
            field=models.BooleanField(auto_created=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='is_medicinal',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plantname',
            name='local_language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
