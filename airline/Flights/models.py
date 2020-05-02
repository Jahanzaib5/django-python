from django.db import models

# Create your models here.
class Airports(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)

	def _str_(self):
		return f"{self.code}--{self.city}"



class Flights(models.Model):
	origin = models.CharField(max_length=64)
	destination = models.CharField(max_length=64)
	duration = models.IntegerField()

	def __str__(self):
		return f"{self.id} - {self.origin} to {self.destination}"