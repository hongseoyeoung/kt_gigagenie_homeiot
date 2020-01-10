from django.urls import path
from . import views

urlpatterns = [
    path('', views.lastsleep, name="lastsleep"),
    path('/detail_bio', views.detail_bio, name="detail_bio"),
    path('/detail_sleep', views.detail_sleep, name="detail_sleep"),
    path('/detail_disease', views.detail_disease, name="detail_disease"),
]