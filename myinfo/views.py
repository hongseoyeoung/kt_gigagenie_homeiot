from django.shortcuts import render
from db import db
# Create your views here.

def myinfo(request):
    myinfo_db = db.select_myinfo(1)

    birth_spl = list(map(int, str(myinfo_db[2]).split("-")))
    birth = str(birth_spl[0]) + "년 " +  str(birth_spl[1]) + "월 " + str(birth_spl[2]) + "일" 
    print(birth)

    if myinfo_db[5] == 0:
        sex = "남자"
    else:
        sex = "여자"
        
    dic = {"name":myinfo_db[1], "birth":birth, "height":myinfo_db[3],
     "weight":myinfo_db[4], "sex":sex, "emgContact": myinfo_db[7]
    }
    return render(request, 'myinfo.html', dic)