# Generated by Django 4.1 on 2022-08-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='cock_type',
            field=models.FloatField(),
        ),
    ]