from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:month>", views.month_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
