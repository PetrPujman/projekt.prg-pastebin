from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"),
path("add/", views.add_item, name="add_item"),
path("account/registration/", views.registration, name="registration"),
]