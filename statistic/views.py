from django.shortcuts import render

# Create your views here.
def statistic(request):
    return render(request, 'statistic.html')

def statistic_bio(request):
    return render(request, 'statistic_bio.html')

def statistic_sleep(request):
    return render(request, 'statistic_sleep.html')

def statistic_disease(request):
    return render(request, 'statistic_disease.html')