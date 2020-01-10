from django.urls import path
from . import views

urlpatterns = [
    path('', views.linked, name="linked"),
    path('/linked_exercise', views.linked_exercise, name="linked_exercise"),
    path('/linked_music', views.linked_music, name="linked_music"),
    path('/linked_food', views.linked_food, name="linked_food")
]