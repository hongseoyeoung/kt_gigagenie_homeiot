from django.shortcuts import render

# Create your views here.
def lastsleep(request):
    return render(request, 'lastsleep.html')
