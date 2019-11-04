from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from . import userDao

# Create your views here.
def realtime(request):
    data = userDao.latest_select()[0]
    hr = data[1]
    rr = data[2]
    sv = data[3]
    hrv = data[4]
    ss = data[5]
    state = data[6]
    return render(request, 'realtime.html', {'hr':hr, 'rr': rr, 'sv':sv, 'hrv':hrv, 'ss':ss, 'state':state})

def ajax(request):
    data = userDao.latest_select()[0]
    hr = data[1]
    rr = data[2]
    sv = data[3]
    hrv = data[4]
    ss = data[5]
    state = data[6]
    context = {'hr' : hr,
                'rr' : rr,
                'sc' : sv,
                'hrv' : hrv,
                'ss' : ss,
                'state' : state}
    return HttpResponse(json.dumps(context), content_type="application/json")