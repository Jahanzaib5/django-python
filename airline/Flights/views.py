from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Flights
# Create your views here.
def index(request):
	context = {
		"flights": Flights.objects.all()
	}
	return render(request, "flights/index.html", context)

def flight(request, flight_id):
	try:
		flight = Flights.objects.get(pk=flight_id)
	except Flights.DoesNotExist:
		raise Http404("Flight doesn't exist")

	context = {
		"flight": flight
	}

	return render(request, "flights/flight.html", context)
