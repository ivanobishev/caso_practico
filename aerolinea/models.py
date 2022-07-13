from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length = 50)
    iata = models.CharField(max_length = 50)
    icao = models.CharField(max_length = 50)
    airport_arrival = models.CharField(max_length = 50)
    iata_arrival = models.CharField(max_length = 50)
    scheduled_arrival = models.DateTimeField()
    airport_departure = models.CharField(max_length = 50)
    iata_departure = models.CharField(max_length = 50)
    scheduled_departure = models.DateTimeField()
