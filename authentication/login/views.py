from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm


# Create your views here.

def index(request):
  if not request.user.is_authenticated:
      return render(request, "users/login.html", {"message": None})
  context = {
      "user": request.user
  }
  return render(request, "users/user.html", context)

def login_view(request):
  username = request.POST["username"]
  password = request.POST["password"]
  user = authenticate(request, username=username, password=password)
  if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse("index"))
  else:
      return render(request, "users/login.html", {"message": "Invalid credentials."})

def check(request):
	if not request.user.is_authenticated:
		return render(request, "users/login.html", {"message": None})
	context = {
		"user": request.user
	}
	return render(request, "users/check.html", context)


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
		    form.save()

		#return HttpResponseRedirect(reverse("index"))
		return render(request, "users/login.html", {"message": "Account Created successfully. Login to continue!"})

	else:
		form = RegisterForm()
		args = {"form": form}
	return render(request, "users/register.html", args)

def logout_view(request):
  logout(request)
  return render(request, "users/login.html", {"message": "Logged out."})