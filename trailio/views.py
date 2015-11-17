from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    ##home page
    return HttpResponse("Hello, world!")

def itinerary_results(request, user_id, itinerary_id):
    ##results for itinerary
    context =
    return render(request, template, context)

def build_itinerary(request, user_id):
    ###page where user builds itinerary
    context =
    return render(request, template, context)

def user_detail(request, user_id):
    #user detailed page
    context = 
    return render(request, template, context)


# Create your views here.
