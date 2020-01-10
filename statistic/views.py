from django.shortcuts import render
from db import db
from db import feature_valueOfHRV

# Create your views here.
def statistic(request):
    return render(request, 'statistic.html')

def statistic_bio(request):
    return render(request, 'statistic_bio.html')

def statistic_sleep(request):
    return render(request, 'statistic_sleep.html')

def statistic_disease(request):
    hrv = []
    result = db.select_bioday(1)
    bio_rt = db.select_bio_RT(1,"2019-11-12")
    for i in bio_rt:
        if i[3] != '0':
            hrv.append(int(i[3]))

    
    sdnn = feature_valueOfHRV.getSDNN(hrv)
    pnn50 = feature_valueOfHRV.getPNN50(hrv) * 1000
    rmssd = feature_valueOfHRV.getRMSSD(hrv)

    bioday = {"hr_mean": result[3], "rr_mean": result[6], "sv_mean": result[9], "hrv_mean": result[12],
            "sdnn" :sdnn, "pnn50":pnn50, "rmssd":rmssd
        }
    return render(request, 'statistic_disease.html', bioday)