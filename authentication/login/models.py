from django.db import models

# Create your models here.


class Course(models.Model):
	name = models.CharField(max_length=64)
	c_type = models.CharField(max_length=10, blank=False, null=False)

	def __str__(self):
		return f"{self.name} -- {self.c_type}"
