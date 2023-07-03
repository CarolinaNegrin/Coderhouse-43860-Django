from django.urls import path

from .views import home

app_name = "usuario"


urlpatterns = [
    path("", home, name="home"),
]