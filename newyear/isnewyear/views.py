from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
	now = datetime.datetime.now()
	return render(request, "isnewyear/index.html", {
		"isnewyear": now.month == 1 and now.day ==1
		})
