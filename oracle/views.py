from django.shortcuts import render
import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.datetime.now()
    return HttpResponse("Hello, world. You've met the oracle index.\n The time: %s" % now)

# Create your views here.
