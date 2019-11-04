from django.shortcuts import render

# Create your views here.
def myinfo(request):
    return render(request, 'myinfo.html')