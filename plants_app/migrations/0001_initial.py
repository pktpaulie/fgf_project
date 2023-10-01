# Generated by Django 4.2.3 on 2023-10-01 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=250)),
                ('scientific_name', models.CharField(max_length=250)),
                ('region', models.CharField(choices=[('', 'Select Region'), ('Northern Uganda', 'Northern Uganda'), ('West Nile', 'West Nile'), ('Central Uganda', 'Central Uganda'), ('Eastern Uganda', 'Eastern Uganda'), ('Western Uganda', 'Western Uganda'), ('All Regions', 'All Regions')], max_length=50)),
                ('unique_habitat', models.CharField(max_length=250)),
                ('life_form', models.CharField(choices=[('', 'Select Life Form'), ('shrub', 'Shrub'), ('tree', 'Tree'), ('herb', 'Herb'), ('grass', 'Grass'), ('climber', 'Climber'), ('other', 'Other')], max_length=250)),
                ('specify_other_life_form', models.CharField(blank=True, max_length=250, null=True)),
                ('value', models.CharField(choices=[('', 'Select Value'), ('ecological', 'Ecological'), ('social', 'Social'), ('economic', 'Economic'), ('nutritional', 'Nutritional'), ('other', 'Other')], max_length=250)),
                ('if_other_value_specify', models.CharField(blank=True, max_length=250, null=True)),
                ('value_details', models.CharField(blank=True, max_length=250, null=True)),
                ('climate_impact', models.CharField(max_length=250)),
                ('research_notes', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('videos', models.FileField(blank=True, null=True, upload_to='media_files')),
                ('audio', models.FileField(blank=True, null=True, upload_to='media_files')),
                ('citation', models.CharField(max_length=250)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('contributor_email', models.EmailField(max_length=254)),
                ('contributor_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="Contributor's phone number", max_length=128, region=None)),
                ('contributor_is_source', models.BooleanField(default=True, help_text='Is the contributor the source of information?')),
                ('source_name', models.CharField(blank=True, help_text="Source's name", max_length=100)),
                ('source_email', models.EmailField(blank=True, help_text="Source's email address", max_length=254)),
                ('source_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="Source's phone number", max_length=128, region=None)),
                ('publish_preference', models.CharField(choices=[('', 'Select Publishing Preference'), ('name_and_email', 'Name and Email'), ('name_only', 'Name Only'), ('none', 'Do Not Publish')], max_length=20)),
                ('contributor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlantName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_names', to='plants_app.plant')),
            ],
        ),
        migrations.CreateModel(
            name='MedicinalPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicinal_values_entered', models.BooleanField(default=False)),
                ('health_issues', models.TextField(blank=True, help_text='Add multiple health issues, separated by commas')),
                ('part_used_for_health_issues', models.TextField(blank=True, help_text='Part of the plant used for each health issue')),
                ('preparation_steps', models.TextField(blank=True, help_text='Preparation steps for each health issue')),
                ('dosage', models.TextField(blank=True, help_text='Dosage for each health issue')),
                ('contraindications', models.TextField(blank=True, help_text='Contraindications for each health issue')),
                ('shelf_life', models.CharField(blank=True, help_text='Shelf life of the prepared medicine', max_length=100)),
                ('notes', models.TextField(blank=True, help_text='Additional notes for medicinal values')),
                ('plant', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants_app.plant')),
            ],
        ),
    ]
