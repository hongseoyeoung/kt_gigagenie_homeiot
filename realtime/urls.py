from django.urls import path
from . import views

urlpatterns = [
    path('', views.realtime, name="realtime"),
    path('ajax', views.ajax, name="ajax"),
]