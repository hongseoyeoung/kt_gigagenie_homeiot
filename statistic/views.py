from django.shortcuts import render

# Create your views here.
def statistic(request):
    return render(request, 'statistic.html')
