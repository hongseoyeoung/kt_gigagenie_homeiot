from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from db import db

# Create your views here.
def realtime(request):
    data = db.latest_select()[0]
    hr = data[3]
    rr = data[4]
    sv = data[5]
    hrv = data[6]
    return render(request, 'realtime.html', {'hr':hr, 'rr': rr, 'sv':sv, 'hrv':hrv})

def ajax(request):
    data = db.latest_select()[0]
    hr = data[3]
    rr = data[4]
    sv = data[5]
    hrv = data[6]
    context = {'hr' : hr,
                'rr' : rr,
                'sv' : sv,
                'hrv' : hrv}
    return HttpResponse(json.dumps(context), content_type="application/json")