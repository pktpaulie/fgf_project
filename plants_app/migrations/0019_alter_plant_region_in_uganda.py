# Generated by Django 4.2.6 on 2023-11-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_app', '0018_alter_plant_region_in_uganda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='region_in_Uganda',
            field=models.CharField(choices=[('northern_uganda', 'Northern Uganda'), ('eastern_uganda', 'Eastern Uganda'), ('western_uganda', 'Western Uganda'), ('central_uganda', 'Central Uganda')], max_length=100, null=True),
        ),
    ]
