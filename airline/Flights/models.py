from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Airports(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.city} ({self.code})" 



class Flights(models.Model):
	origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="departures")
	destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='arrivals')
	duration = models.IntegerField()

	def __str__(self):
		return f"{self.id} - {self.origin} to {self.destination}"

class Passenger(models.Model):
	first = models.CharField(max_length=64)
	last = models.CharField(max_length=64)
	flights = models.ManyToManyField(Flights, blank=True, related_name='passengers')

	def __str__(self):
		return f"{self.first} {self.last}"


class Course(models.Model):
	name = models.CharField(max_length=64)
	c_type = models.CharField(max_length=10, blank=False, null=False)

	def __str__(self):
		return f"{self.name} -- {self.c_type}"


class Course_taken(models.Model):
	user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="User")
	taken = models.ForeignKey(Course, blank=False, null=False, on_delete=models.CASCADE, related_name="Taken")
	#user_r = models.ManyToManyField(User, blank=True, related_name='c_user')
	#taken_r = models.ManyToManyField(Course, blank=True, related_name='c_taken')

	def __str__(self):
		return f"{self.user} -- {self.taken}"


