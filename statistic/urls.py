from django.urls import path
from . import views

urlpatterns = [
    path('', views.statistic, name="statistic"),
    path('/statistic_bio', views.statistic_bio, name="statistic_bio"),
    path('/statistic_sleep', views.statistic_sleep, name="statistic_sleep"),
    path('/statistic_disease', views.statistic_disease, name="statistic_disease")
]