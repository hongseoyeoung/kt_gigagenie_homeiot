from django.shortcuts import render
from . import db
from . import feature_valueOfHRV
import numpy as np
# Create your views here.
def lastsleep(request):
    ########################## db에서 데이터 받아 오기 #########################
    result = db.select_bioday(1)
    bio_rt = db.select_bio_RT(1,"2019-11-12")
    hr = []
    hrv = []
    hr_hour = []
    for i in bio_rt:
        hr.append(int(i[0]))
        if i[1] != '0':
            hrv.append(int(i[1]))
    ########################### hr 그래프 그리기 ############################# 
    interval = 600
    sec = 0
    while sec + interval <= len(hr):
        mean = 0
        zero_c = 0
        for i in range(sec,sec+interval):
            if hr[i] == 0:
                zero_c += 1
                continue
            mean += hr[i]
        
        if interval == zero_c:
            hr_hour.append(0)
        else:
            hr_hour.append(mean/(interval-zero_c))
        sec += interval
    
    mean = 0
    zero_c = 0
    for i in range(sec,len(hr)):
        if hr[i] == 0:
            zero_c += 1
            continue
        mean += hr[i]
    if len(hr) - sec == zero_c:
        hr_hour.append(0)
    else:
        hr_hour.append(mean/(len(hr)-sec-zero_c))

    labels = []
    for i in range(0, (len(hr)//interval)+1):
        labels.append(i*interval//60)
    ################### hrv 통계 SDNN, pNN50, RMSSD ####################
    sdnn = feature_valueOfHRV.getSDNN(hrv)
    pnn50 = feature_valueOfHRV.getPNN50(hrv) * 1000
    rmssd = feature_valueOfHRV.getRMSSD(hrv)
    
    normalize = []
    for i in range(1,5):
        high = int(result[i*3+1])
        low = int(result[i*3+2])
        normalize.append((int(result[i*3]) - low) / (high - low) * 100)


    ################### 전송할 데이터 딕셔너리화 ######################
    bioday = {"hr_mean": result[3], "rr_mean": result[6], "sv_mean": result[9], "hrv_mean": result[12], "hr_hour": hr_hour, "hr_labels":labels,
            "sdnn" :sdnn, "pnn50":pnn50, "rmssd":rmssd
        }
    return render(request, 'lastsleep.html', bioday)

def detail_bio(request):
    result = db.select_bioday(1)
    bio_rt = db.select_bio_RT(1,"2019-11-12")
    hr = []
    hrv = []
    hr_hour = []
    for i in bio_rt:
        hr.append(int(i[0]))
        if i[1] != '0':
            hrv.append(int(i[1]))
            
    interval = 600
    sec = 0
    while sec + interval <= len(hr):
        mean = 0
        zero_c = 0
        for i in range(sec,sec+interval):
            if hr[i] == 0:
                zero_c += 1
                continue
            mean += hr[i]
        
        if interval == zero_c:
            hr_hour.append(0)
        else:
            hr_hour.append(mean/(interval-zero_c))
        sec += interval
    
    mean = 0
    zero_c = 0
    for i in range(sec,len(hr)):
        if hr[i] == 0:
            zero_c += 1
            continue
        mean += hr[i]
    if len(hr) - sec == zero_c:
        hr_hour.append(0)
    else:
        hr_hour.append(mean/(len(hr)-sec-zero_c))

    labels = []
    for i in range(0, (len(hr)//interval)+1):
        labels.append(i*interval//60)
    bioday = {"hr_mean": result[3], "rr_mean": result[6], "sv_mean": result[9], "hrv_mean": result[12], "hr_hour": hr_hour, "hr_labels":labels,}
    return render(request, 'detail_bio.html', bioday)

def detail_sleep(request):
    return render(request, 'detail_sleep.html')

def detail_disease(request):
    return render(request, 'detail_disease.html')