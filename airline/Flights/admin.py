from django.contrib import admin

from .models import Airports, Flights

# Register your models here.

admin.site.register(Airports)
admin.site.register(Flights)