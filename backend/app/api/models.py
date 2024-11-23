from django.db import models


# Create your models here.
class Parking(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    nom = models.CharField(max_length=50)


class Planta(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)


class Plaza(models.Model):
    id = models.AutoField(primary_key=True)
    ocupada = models.BooleanField()
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)


class PlazaLog(models.Model):
    id = models.AutoField(primary_key=True)
    datahora = models.DateTimeField()
    plaza = models.ForeignKey(Plaza, on_delete=models.CASCADE)
