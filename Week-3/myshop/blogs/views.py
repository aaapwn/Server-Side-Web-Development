from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta
from django.utils import timezone
# Create your views here.

def index(request):
    time = timezone.localtime() + timedelta(days=500)
    day =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return HttpResponse(str(time) + " | " + day[time.weekday()])

