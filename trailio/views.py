from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world!")

def itinerary_results(request, user_id, itinerary_id):
    return None

def build_itinerary(request, user_id):
    return None

def user_detail(request, user_id):
    return None


# Create your views here.
