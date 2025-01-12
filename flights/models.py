from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='saida')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='chegada')
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} duration of {self.duration}."
    
class Passanger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flight, blank=True, related_name='passanger')

    def __str__(self) -> str:
        return f"{self.first} {self.last}"
