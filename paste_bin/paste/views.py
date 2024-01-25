from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ContentForm
from django.contrib import messages
from .models import Content


def index(request):
	contents = Content.objects.filter(user_id=request.user.id)
	return render(request, "index.html", {"contents": contents})


def registration(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect("login")
	else:
		form = UserCreationForm()
	return render(request, "registration/registration.html", {"form": form})


@login_required
def add_item(request):
	if request.method == "POST":
		form = ContentForm(request.POST)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.add_message(request, messages.INFO, "text byl přidán.")
			return redirect("index")
	else:
		form = ContentForm()

	return render(request, "add_item.html", {"form": form})
