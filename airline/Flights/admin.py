from django.contrib import admin

from .models import Airports, Flights, Passenger, Course, Course_taken

# Register your models here.

admin.site.register(Airports)
admin.site.register(Flights)
admin.site.register(Passenger)
admin.site.register(Course)
admin.site.register(Course_taken)