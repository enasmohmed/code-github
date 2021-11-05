from django.urls import path, re_path

from properties import views

app_name = 'properties'

urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:slug>/", views.nav, name="dox_detail"),
]
