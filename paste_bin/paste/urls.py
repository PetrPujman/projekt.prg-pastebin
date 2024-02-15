from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_item, name="add_item"),
    path("account/registration/", views.registration, name="registration"),
    path("content/<slug:slug>", views.display_content, name="display_content"),
    path("delete/<int:content_id>", views.remove_item, name="remove_item"),
]
