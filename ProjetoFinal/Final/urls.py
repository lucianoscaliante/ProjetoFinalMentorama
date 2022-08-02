from django.urls import path

from . import views

app_main = "Final"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
