from django.db import models


class CarModel(models.Model):
    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seats = models.IntegerField()
    cock_type = models.CharField(max_length=25)
    engine_vol = models.FloatField()

    class Meta:
        db_table = 'cars'
