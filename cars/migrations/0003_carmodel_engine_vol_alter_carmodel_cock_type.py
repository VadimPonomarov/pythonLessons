# Generated by Django 4.1 on 2022-08-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carmodel_cock_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='engine_vol',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='cock_type',
            field=models.CharField(max_length=25),
        ),
    ]