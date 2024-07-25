from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta
from django.utils import timezone
# Create your views here.

def index(request):
    time = timezone.localtime() + timedelta(days=500)
    s = time.strftime("%A -%d/%m/%Y, %H:%M:%S")
    return HttpResponse(str(s))

