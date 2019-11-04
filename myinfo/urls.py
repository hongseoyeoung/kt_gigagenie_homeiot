from django.urls import path
from . import views

urlpatterns = [
    path('', views.myinfo, name="myinfo")
]