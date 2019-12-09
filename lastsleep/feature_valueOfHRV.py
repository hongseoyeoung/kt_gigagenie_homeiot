import numpy as np
from . import db
'''
DB에서 읽어오는걸로 바꿔
'''
#data=pd.read_csv("C:/Users/Administrator/Desktop/temp/data/rawdata/mj.csv", sep=",")

'''
SDNN : 표준편차
'''
def getSDNN(df):
    sdnn=round(float(np.std(df)), 2) # 읽어온 데이터 중 HRV의 표준편차를 구함

    return sdnn

'''
SDANN : 5분간격의 HRV 평균에 대한 표준편차, 장기적 관찰에 좋음
'''
def getSDANN(df):
    tmp=list()  # 5분 간격의 HRV 평균이 들어갈 리스트, 1시간이면 12개의 값이 들어감

    term=0 # 5분 간격의 평균 값의 개수를 세기 위한 변수
    start=0 # 5분 간격의 처음
    end=299  # 5분 간격의 끝

    while(start<len(df)):
        tmp.append(round(float(np.mean(df[start:end+1])), 2)) # 5분 간격의 평균을 리스트에 저장

        if len(tmp) > int(len(df)/300): # 5분 간격 즉 300개가 안채워지는 건 잘라버림
            tmp=tmp[:int(len(df)/300)]

        start+=300
        end+=300

    sdann=np.std(tmp, ddof=True) # 5분 간격 평균에 대한 표준편차

    return sdann

'''
RMSSD : 인접한 HRV의 차이에 대한 제곱의 합을 평균하여 이에대한 제곱근으로 표현한 것
'''
def getRMSSD(df):
    tmp=list()

    for i in range(0, len(df)-1):
        tmp.append(pow((df[i]-df[i+1]), 2)) # 인접한 HRV의 차이에 대한 제곱의 합을 tmp 리스트에 저장

    rmssd=round(np.sqrt(sum(tmp)/(len(df)-1)), 2) # 평균내서 제곱근으로 표현

    return rmssd

'''
pNN50 : HRV간격의 차가 50ms가 넘는 것의 개수에 대한 백분율
'''
def getPNN50(df):
    tmp=list()

    for i in range(0, len(df)-1):
        if i is 0:
            tmp.append(0) # 제일 첫번째 값은 비교할 값이 없으므로 0을 삽입
        else:
            tmp.append(abs(df[i]-df[i+1])) # HRV 간격의 차를 넣음

    cnt_50ms=0 # 간격의 차가 50ms가 넘는 것의 개수를 셀 변수

    for i in range(0, len(tmp)): # 50ms인 것 찾아서 카운트
        if tmp[i]>50:
            cnt_50ms+=1

    pNN50=round((cnt_50ms/(len(df)-1)), 3) # 전체 HRV 간격 중 HRV 간격이 50ms넘는 비율 구함

    return pNN50

'''
Execute 
'''
#print(getSDNN(data))
#print(getSDANN(data))
#print(getRMSSD(data))
#print(getNN(data))