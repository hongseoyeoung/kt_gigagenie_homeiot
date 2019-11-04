from django.urls import path
from . import views

urlpatterns = [
    path('', views.linked, name="linked")
]