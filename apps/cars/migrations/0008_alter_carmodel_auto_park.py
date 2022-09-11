# Generated by Django 4.1 on 2022-09-11 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
        ('cars', '0007_alter_carmodel_auto_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel'),
        ),
    ]
