# Generated by Django 4.2.5 on 2023-10-11 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animallocalname',
            old_name='local_name',
            new_name='animal_name',
        ),
        migrations.AlterField(
            model_name='animallocalname',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_names', to='animals_app.animal'),
        ),
    ]