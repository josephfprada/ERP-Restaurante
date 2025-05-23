from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.home, name="home"),
    path("main/", views.home, name="login"),
    path("main/create/", views.create, name="create"),
]