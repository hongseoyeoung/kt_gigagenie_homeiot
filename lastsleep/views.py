from django.shortcuts import render
from db import db
from db import feature_valueOfHRV
from db import draw_graph

# Create your views here.
def lastsleep(request):
    ########################## db에서 데이터 받아 오기 #########################
    draw_graph.get_feature_of_hrv(1,'2020-01-08')
    result = db.select_bioday(1)
    bio_rt = db.select_bio_RT(1,"2019-11-12")
    hr = []
    rr = []
    sv = []
    hrv = []
    hrv_mean = []
    hr_hour = []
    for i in bio_rt:
        hr.append(int(i[0]))
        rr.append(int(i[1]))
        sv.append(int(i[2]))
        hrv.append(int(i[3]))

        if i[3] != '0':
            hrv_mean.append(int(i[3]))
    ########################### hr 그래프 그리기 ############################# 
    interval = 3600
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
    sdnn = feature_valueOfHRV.getSDNN(hrv_mean)
    pnn50 = feature_valueOfHRV.getPNN50(hrv_mean) * 1000
    rmssd = feature_valueOfHRV.getRMSSD(hrv_mean)

    ################### 전송할 데이터 딕셔너리화 ######################
    bioday = {"hr_mean": int(result[3]), "rr_mean": int(result[6]), "sv_mean": int(result[9]), "hrv_mean": int(result[12]), "hr_hour": hr_hour, "hr_labels":labels,
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
    return render(request, 'detail_disease.html', bioday)