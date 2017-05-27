from django.shortcuts import render, HttpResponse
import time
# Create your views here.

def displayDateAndTime(request):
    DT = {
    'time': time.strftime('%I:%M:%S %p'),
    'date': time.strftime('%m/%d/%Y')
    }
    return render(request, 'timedisplay/index.html', DT)
