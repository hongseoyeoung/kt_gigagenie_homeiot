from django.shortcuts import render

# Create your views here.
def linked(request):
    return render(request, 'linked.html')

def linked_exercise(request):
    return render(request, 'linked_exercise.html')

def linked_music(request):
    return render(request, 'linked_music.html')

def linked_food(request):
    return render(request, 'linked_food.html')